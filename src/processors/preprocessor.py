"""
src/processors/preprocessor.py
─────────────────────────────────
Phase 4: Preprocessing. Validates schema, strips HTML from bodies, and
normalizes published dates to YYYY-MM-DD.
"""

import logging
import re
from datetime import datetime

from bs4 import BeautifulSoup

logger = logging.getLogger("research_agent")

REQUIRED_FIELDS = ("source", "title", "url")
_ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_DATE_FORMATS = (
    "%a, %d %b %Y %H:%M:%S %z",
    "%a, %d %b %Y %H:%M:%S %Z",
    "%Y-%m-%dT%H:%M:%S%z",
    "%B %d, %Y",
    "%b %d, %Y",
)


def _strip_html(text: str) -> str:
    if not text:
        return ""
    return BeautifulSoup(text, "html.parser").get_text(separator=" ", strip=True)


def _normalize_date(raw_date: str) -> str:
    raw_date = (raw_date or "").strip()
    if not raw_date:
        return datetime.utcnow().strftime("%Y-%m-%d")
    if _ISO_RE.match(raw_date):
        return raw_date
    for fmt in _DATE_FORMATS:
        try:
            return datetime.strptime(raw_date, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return datetime.utcnow().strftime("%Y-%m-%d")


def preprocess(raw_articles):
    clean = []
    for article in raw_articles:
        if not all(article.get(f) for f in REQUIRED_FIELDS):
            continue  # drop malformed entries rather than crash later stages

        clean.append({
            "source": article["source"],
            "title": article["title"].strip(),
            "url": article["url"].strip(),
            "published": _normalize_date(article.get("published", "")),
            "body": _strip_html(article.get("body", "")),
        })

    logger.info(f"Preprocessing: {len(raw_articles)} raw -> {len(clean)} valid articles.")
    return clean
