"""
config/settings.py
────────────────────
Centralized configuration, loaded from environment variables / .env.
Every field here matches what app.py's Configuration tab writes via
save_env_values(), so saving settings there just works.

NOTE ON SOURCES: OpenAI, Hugging Face and TechCrunch have real public RSS
feeds. Anthropic and Product Hunt do not, so those two are scraped
directly from their pages in src/collectors/rss_collector.py — the most
likely place a fix is needed later if either site's layout changes.
"""

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_DELAY_SECONDS = float(os.getenv("GEMINI_DELAY_SECONDS", "4"))

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "")
GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH", "credentials.json")

DUPLICATE_THRESHOLD = float(os.getenv("DUPLICATE_THRESHOLD", "90"))

DATA_DIR = os.getenv("DATA_DIR", "data")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
REPORTS_DIR = os.path.join(DATA_DIR, "reports")

ANALYZED_ARTICLES_PATH = os.path.join(PROCESSED_DIR, "analyzed_articles.json")
THEMES_PATH = os.path.join(PROCESSED_DIR, "themes.json")

DIGEST_MD_PATH = os.path.join(REPORTS_DIR, "weekly_digest.md")
DIGEST_PDF_PATH = os.path.join(REPORTS_DIR, "weekly_digest.pdf")

DEMO_MODE_ARTICLE_LIMIT = 3

# Real public RSS feeds
RSS_SOURCES = {
    "OpenAI": "https://openai.com/news/rss.xml",
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
    "TechCrunch": "https://techcrunch.com/category/artificial-intelligence/feed/",
}
# No public RSS feed for these two — scraped directly (best-effort, see collector).
ANTHROPIC_NEWS_URL = "https://www.anthropic.com/news"
PRODUCT_HUNT_AI_URL = "https://www.producthunt.com/categories/artificial-intelligence"

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)
