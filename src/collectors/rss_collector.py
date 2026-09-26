"""
src/collectors/rss_collector.py
─────────────────────────────────
Phase 3: Collection. Pulls raw articles from RSS feeds (feedparser) and
scrapes the two sources without a stable public RSS feed (BeautifulSoup).

Every source is wrapped in try/except: one source failing (dead feed, site
redesign, network issue) must not crash the whole pipeline, per the
README's "Non-Blocking Integrations" resiliency requirement.
"""

import logging
import time

import requests
from bs4 import BeautifulSoup
import feedparser

from config.settings import RSS_SOURCES, ANTHROPIC_NEWS_URL, PRODUCT_HUNT_AI_URL

logger = logging.getLogger("research_agent")

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AIResearchAgent/1.0)"}


def _collect_rss(source_name: str, feed_url: str):
    articles = []
    try:
        parsed = feedparser.parse(feed_url)
        for entry in parsed.entries:
            struct = entry.get("published_parsed") or entry.get("updated_parsed")
            published = time.strftime("%Y-%m-%d", struct) if struct else entry.get("published", "")
            articles.append({
                "source": source_name,
                "title": entry.get("title", "").strip(),
                "url": entry.get("link", ""),
                "published": published,
                "body": entry.get("summary", entry.get("description", "")),
            })
    except Exception as e:
        logger.warning(f"RSS collection failed for {source_name}: {e}")
    return articles


def _dedupe_by_url(articles):
    seen, unique = set(), []
    for a in articles:
        if a["url"] and a["url"] not in seen:
            seen.add(a["url"])
            unique.append(a)
    return unique


def _collect_anthropic():
    """Anthropic has no public RSS feed; scrape the news index page instead."""
    articles = []
    try:
        resp = requests.get(ANTHROPIC_NEWS_URL, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for link in soup.select("a[href*='/news/']"):
            title = link.get_text(strip=True)
            href = link.get("href", "")
            if not title or not href:
                continue
            url = href if href.startswith("http") else f"https://www.anthropic.com{href}"
            articles.append({"source": "Anthropic", "title": title, "url": url, "published": "", "body": ""})
    except Exception as e:
        logger.warning(f"Anthropic scrape failed (site layout may have changed): {e}")
    return _dedupe_by_url(articles)


def _collect_product_hunt():
    """Product Hunt's AI category has no stable public feed; best-effort scrape."""
    articles = []
    try:
        resp = requests.get(PRODUCT_HUNT_AI_URL, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for link in soup.select("a[href*='/products/']"):
            title = link.get_text(strip=True)
            href = link.get("href", "")
            if not title or not href:
                continue
            url = href if href.startswith("http") else f"https://www.producthunt.com{href}"
            articles.append({"source": "Product Hunt", "title": title, "url": url, "published": "", "body": ""})
    except Exception as e:
        logger.warning(f"Product Hunt scrape failed (site layout may have changed): {e}")
    return _dedupe_by_url(articles)


def collect_all():
    """Run every collector and return the combined raw article list."""
    all_articles = []
    for name, url in RSS_SOURCES.items():
        all_articles.extend(_collect_rss(name, url))
    all_articles.extend(_collect_anthropic())
    all_articles.extend(_collect_product_hunt())
    logger.info(f"Collected {len(all_articles)} raw articles from {len(RSS_SOURCES) + 2} sources.")
    return all_articles
