"""
src/agents/theme_agent.py
─────────────────────────────
Phase 8: Theme Detection. Aggregates weekly statistics and asks Gemini to
identify the top recurring themes across all analyzed articles.

total_articles / duplicates_removed are accepted as optional params because
this agent only ever sees the *unique* article list — the raw and duplicate
counts live one step earlier in the pipeline (in app.py's Run Pipeline page,
or in ResearchAgent.run()). Passing them in keeps statistics.json accurate
from both call sites instead of silently defaulting to 0.
"""

import json
import logging
import re
from collections import Counter
from datetime import datetime

import google.generativeai as genai

from config.settings import GEMINI_API_KEY, GEMINI_MODEL

logger = logging.getLogger("research_agent")

_THEME_PROMPT = """Below are the titles and categories of this week's AI news articles. \
Identify the top 3-5 recurring themes across them. Respond with ONLY a JSON object \
(no markdown fences): {{"top_themes": ["theme 1", "theme 2", ...]}}

Articles:
{article_list}
"""


class ThemeAgent:
    def __init__(self):
        self._configured = bool(GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL) if self._configured else None
        if self._configured:
            genai.configure(api_key=GEMINI_API_KEY)

    def _detect_top_themes(self, articles):
        if not self._configured or not articles:
            return []
        article_list = "\n".join(
            f"- [{a.get('category', 'Other')}] {a.get('title', '')}" for a in articles[:40]
        )
        try:
            response = self.model.generate_content(_THEME_PROMPT.format(article_list=article_list))
            text = re.sub(r"^```(?:json)?|```$", "", (response.text or "").strip(), flags=re.MULTILINE)
            return json.loads(text.strip()).get("top_themes", [])[:5]
        except Exception as e:
            logger.warning(f"Theme detection failed, falling back to category counts: {e}")
            return []

    def detect_themes(self, analyzed_articles: list, total_articles: int = None, duplicates_removed: int = 0) -> dict:
        categories = Counter(a.get("category", "Other") for a in analyzed_articles)
        companies = Counter()
        for a in analyzed_articles:
            companies.update(a.get("companies", []))

        top_themes = self._detect_top_themes(analyzed_articles) or [c for c, _ in categories.most_common(5)]

        dates = [a.get("published", "") for a in analyzed_articles if a.get("published")]
        today = datetime.utcnow().strftime("%Y-%m-%d")

        return {
            "themes": {
                "top_themes": top_themes,
                "top_categories": dict(categories.most_common(5)),
                "top_companies": dict(companies.most_common(10)),
            },
            "statistics": {
                "total_articles": total_articles if total_articles is not None else len(analyzed_articles),
                "unique_articles": len(analyzed_articles),
                "duplicates_removed": duplicates_removed,
                "date_range": {"start": min(dates) if dates else today, "end": max(dates) if dates else today},
            },
        }
