"""
src/processors/deduplicator.py
─────────────────────────────────
Phase 5: Duplicate Detection. Computes Levenshtein-based title similarity
via RapidFuzz and filters out near-duplicate articles (>= threshold %).
"""

import logging

from rapidfuzz import fuzz

from config.settings import DUPLICATE_THRESHOLD

logger = logging.getLogger("research_agent")


def remove_duplicates(articles, threshold: float = None):
    threshold = threshold if threshold is not None else DUPLICATE_THRESHOLD

    unique = []
    duplicates = []

    for article in articles:
        is_dup = False
        for kept in unique:
            if fuzz.ratio(article["title"].lower(), kept["title"].lower()) >= threshold:
                is_dup = True
                break
        (duplicates if is_dup else unique).append(article)

    logger.info(
        f"Deduplication: {len(articles)} -> {len(unique)} unique "
        f"({len(duplicates)} duplicates removed at {threshold}% threshold)."
    )
    return unique, duplicates
