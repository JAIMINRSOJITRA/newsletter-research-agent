"""
src/storage/storage_manager.py
──────────────────────────────────
Phase 7: Storage. Saves local JSON backups and (optionally) syncs analyzed
rows to a Google Sheet via a service account. The Sheets sync is wrapped in
try/except and is entirely optional — a missing/invalid credentials.json or
GOOGLE_SHEET_ID just logs a warning and the pipeline continues, per the
README's "Non-Blocking Integrations" resiliency requirement.

SETUP NEEDED FOR SHEETS SYNC (not included — these are account-specific):
  1. Create a Google Cloud service account, enable the Sheets API.
  2. Download its JSON key and save it as credentials.json at the repo root
     (path is configurable via GOOGLE_CREDENTIALS_PATH).
  3. Share your target Google Sheet with the service account's email address.
  4. Set GOOGLE_SHEET_ID in .env / the Configuration tab.
Without all four, sync is silently skipped and everything else still works.
"""

import json
import logging
import os

from config.settings import GOOGLE_SHEET_ID, GOOGLE_CREDENTIALS_PATH, ANALYZED_ARTICLES_PATH, THEMES_PATH

logger = logging.getLogger("research_agent")


def save_analyzed_articles(analyzed_articles: list):
    os.makedirs(os.path.dirname(ANALYZED_ARTICLES_PATH), exist_ok=True)
    with open(ANALYZED_ARTICLES_PATH, "w", encoding="utf-8") as f:
        json.dump(analyzed_articles, f, indent=2, ensure_ascii=False)
    logger.info(f"Saved {len(analyzed_articles)} analyzed articles to {ANALYZED_ARTICLES_PATH}")


def save_themes(themes: dict):
    os.makedirs(os.path.dirname(THEMES_PATH), exist_ok=True)
    with open(THEMES_PATH, "w", encoding="utf-8") as f:
        json.dump(themes, f, indent=2, ensure_ascii=False)
    logger.info(f"Saved theme statistics to {THEMES_PATH}")


def sync_to_google_sheets(analyzed_articles: list):
    if not GOOGLE_SHEET_ID:
        logger.info("GOOGLE_SHEET_ID not set; skipping Google Sheets sync.")
        return
    if not os.path.exists(GOOGLE_CREDENTIALS_PATH):
        logger.warning(f"{GOOGLE_CREDENTIALS_PATH} not found; skipping Google Sheets sync.")
        return
    if not analyzed_articles:
        return

    try:
        import gspread
        from google.oauth2.service_account import Credentials

        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_PATH, scopes=scopes)
        sheet = gspread.authorize(creds).open_by_key(GOOGLE_SHEET_ID).sheet1

        header = list(analyzed_articles[0].keys())
        if not sheet.get_all_values():
            sheet.append_row(header)

        rows = [
            [", ".join(v) if isinstance(v, list) else str(v) for v in (a.get(h, "") for h in header)]
            for a in analyzed_articles
        ]
        sheet.append_rows(rows)
        logger.info(f"Synced {len(rows)} rows to Google Sheet {GOOGLE_SHEET_ID}.")
    except Exception as e:
        logger.warning(f"Google Sheets sync failed (continuing without it): {e}")


def store(analyzed_articles: list):
    save_analyzed_articles(analyzed_articles)
    sync_to_google_sheets(analyzed_articles)
