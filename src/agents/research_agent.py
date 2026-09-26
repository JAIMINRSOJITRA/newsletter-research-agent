"""
src/agents/research_agent.py
────────────────────────────────
Orchestrates the full pipeline described in README.md, exposing both:
  - Granular step methods (collect/preprocess/remove_duplicates/store/
    generate_digest, plus .analyzer and .theme_agent) used by app.py's
    "Run Pipeline" page for live per-phase progress.
  - A single .run() method used by main.py's CLI entry point.

Both paths converge on the same theme/statistics contract
(ThemeAgent.detect_themes) so data/processed/themes.json is always
correct regardless of which entry point produced it.
"""

import logging

from src.collectors.rss_collector import collect_all
from src.processors.preprocessor import preprocess as _preprocess
from src.processors.deduplicator import remove_duplicates as _remove_duplicates
from src.agents.analyzer import Analyzer
from src.agents.theme_agent import ThemeAgent
from src.storage import storage_manager
from src.generators.digest_generator import generate_digest as _generate_digest
from config.settings import DEMO_MODE_ARTICLE_LIMIT

logger = logging.getLogger("research_agent")


class ResearchAgent:
    def __init__(self, demo_mode: bool = False):
        self.demo_mode = demo_mode
        self.analyzer = Analyzer()
        self.theme_agent = ThemeAgent()

    # ---- granular steps (used directly by the Streamlit "Run Pipeline" page) ----

    def collect(self):
        articles = collect_all()
        return articles[:DEMO_MODE_ARTICLE_LIMIT] if self.demo_mode else articles

    def preprocess(self, raw_articles):
        return _preprocess(raw_articles)

    def remove_duplicates(self, clean_articles):
        return _remove_duplicates(clean_articles)

    def store(self, analyzed_articles):
        storage_manager.store(analyzed_articles)

    def generate_digest(self, analyzed_articles, themes):
        return _generate_digest(analyzed_articles, themes)

    # ---- single-call orchestration (used by main.py) ----

    def run(self) -> dict:
        errors = []
        total_articles = 0
        unique_count = 0
        duplicates_count = 0
        analyzed_articles = []
        digest_path = None
        success = False

        try:
            raw_articles = self.collect()
            total_articles = len(raw_articles)

            clean_articles = self.preprocess(raw_articles)
            unique_articles, duplicates = self.remove_duplicates(clean_articles)
            unique_count = len(unique_articles)
            duplicates_count = len(duplicates)

            for article in unique_articles:
                try:
                    analyzed_articles.append(self.analyzer.analyze_article(article))
                except Exception as e:
                    errors.append(f"Analysis failed for '{article.get('title')}': {e}")

            try:
                self.store(analyzed_articles)
            except Exception as e:
                errors.append(f"Storage step failed: {e}")

            try:
                themes = self.theme_agent.detect_themes(
                    analyzed_articles, total_articles=total_articles, duplicates_removed=duplicates_count
                )
                storage_manager.save_themes(themes)
            except Exception as e:
                errors.append(f"Theme detection failed: {e}")
                themes = {
                    "themes": {"top_themes": []},
                    "statistics": {
                        "total_articles": total_articles, "unique_articles": unique_count,
                        "duplicates_removed": duplicates_count, "date_range": {"start": "", "end": ""},
                    },
                }

            try:
                digest_path = self.generate_digest(analyzed_articles, themes)
            except Exception as e:
                errors.append(f"Digest generation failed: {e}")

            success = bool(analyzed_articles) and digest_path is not None

        except Exception as e:
            logger.critical(f"Pipeline failed before analysis stage: {e}", exc_info=True)
            errors.append(str(e))

        return {
            "success": success,
            "total_articles": total_articles,
            "unique_articles": unique_count,
            "analyzed_articles": len(analyzed_articles),
            "digest_path": digest_path,
            "errors": errors,
        }
