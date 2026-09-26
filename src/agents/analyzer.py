"""
src/agents/analyzer.py
─────────────────────────
Phase 6: AI Analysis. Sends each article to Gemini and requests a
structured JSON summary (category, importance, companies, products).
Falls back to safe schema defaults on any parsing/API failure, per the
README's "AI Error Recovery" resiliency requirement.
"""

import json
import logging
import re

import google.generativeai as genai

from config.settings import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_DELAY_SECONDS

logger = logging.getLogger("research_agent")

_PROMPT_TEMPLATE = """You are analyzing a single AI-industry news article for a weekly \
research digest. Respond with ONLY a JSON object (no markdown fences, no commentary) \
with exactly these fields:

{{
  "summary": "2-3 sentence plain-English summary",
  "category": "one of: Model Release, Research, Funding, Product Launch, Policy, Other",
  "importance": "one of: High, Medium, Low",
  "companies": ["list", "of", "company names mentioned"],
  "products": ["list", "of", "product names mentioned"]
}}

Title: {title}
Source: {source}
Content: {body}
"""

_DEFAULT_ANALYSIS = {
    "summary": "Summary unavailable (AI analysis failed for this article).",
    "category": "Other",
    "importance": "Low",
    "companies": [],
    "products": [],
}


def _strip_fences(text: str) -> str:
    return re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()


class Analyzer:
    def __init__(self):
        self.delay = GEMINI_DELAY_SECONDS
        self._configured = bool(GEMINI_API_KEY)
        if self._configured:
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel(GEMINI_MODEL)
        else:
            self.model = None

    def analyze_article(self, article: dict) -> dict:
        result = dict(article)
        if not self._configured:
            logger.warning("Gemini API key not configured; using default analysis schema.")
            result.update(_DEFAULT_ANALYSIS)
            return result

        prompt = _PROMPT_TEMPLATE.format(
            title=article.get("title", ""),
            source=article.get("source", ""),
            body=(article.get("body", "") or "")[:4000],
        )

        try:
            response = self.model.generate_content(prompt)
            parsed = json.loads(_strip_fences(response.text or ""))

            result["summary"] = parsed.get("summary", _DEFAULT_ANALYSIS["summary"])
            result["category"] = parsed.get("category", _DEFAULT_ANALYSIS["category"])
            result["importance"] = parsed.get("importance", _DEFAULT_ANALYSIS["importance"])
            result["companies"] = parsed.get("companies") or []
            result["products"] = parsed.get("products") or []
        except Exception as e:
            logger.warning(f"Gemini analysis failed for '{article.get('title')}': {e}")
            result.update(_DEFAULT_ANALYSIS)

        return result
