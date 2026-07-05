# AI Research Agent - Blueprint Summary

## 🎯 Project at a Glance

**Goal**: Automate AI news collection → analysis → newsletter generation

**Timeline**: 2 days

**Tech Stack**: Python 3.12 + Gemini API

**Output**: Professional weekly AI newsletter (Markdown + PDF)

---

## 📊 10 Implementation Phases

```
Phase 1: Project Setup
  └─> Folder structure + Git + Virtual env + Dependencies

Phase 2: Configuration
  └─> config/sources.py (5+ sources)

Phase 3: Collection (CollectorAgent)
  └─> RSS + Blog scrapers → data/raw/articles.json

Phase 4: Preprocessing (Preprocessor)
  └─> Clean HTML, normalize dates → data/processed/clean_articles.json

Phase 5: Duplicate Detection (DuplicateChecker)
  └─> Title similarity (rapidfuzz) → data/processed/unique_articles.json

Phase 6: AI Analysis (AnalyzerAgent + Gemini)
  └─> Structured extraction → data/processed/analyzed_articles.json

Phase 7: Storage (StorageAgent)
  └─> JSON backup + Google Sheets

Phase 8: Theme Detection (ThemeAgent + Gemini)
  └─> Weekly themes + statistics → data/processed/themes.json

Phase 9: Digest Generation (DigestAgent)
  └─> Markdown + PDF → data/reports/weekly_digest.pdf

Phase 10: Web UI ⭐ (Streamlit)
  └─> app.py → Interactive dashboard, analytics, live pipeline

Phase 11: Documentation
  └─> README + Builder's Note + Diagrams
```

---

## 🏗️ System Architecture (Simplified)

```
USER
  ↓
ResearchAgent (main.py)
  ↓
┌────────────┬────────────┬────────────┬────────────┐
↓            ↓            ↓            ↓            ↓
Collector  Preprocessor Duplicate  Analyzer   Storage
Agent      Agent        Checker    Agent      Agent
  ↓            ↓            ↓            ↓            ↓
RSS/Blog    Clean       Remove     Gemini     JSON +
Scraping    + Validate  Similar    Analysis   Sheets
  ↓            ↓            ↓            ↓            ↓
────────────────────────────────────────────────────────
  ↓                                                   ↓
ThemeAgent                                      DigestAgent
  ↓                                                   ↓
Gemini (themes) + Python (stats)              Markdown → PDF
  ↓                                                   ↓
themes.json                                   weekly_digest.pdf
```

---

## 📦 Data Flow (End-to-End)

```
config/sources.py (5 sources)
  ↓
COLLECT (feedparser + requests + BeautifulSoup)
  ↓
data/raw/articles.json (30 raw articles)
  ↓
CLEAN (remove HTML, normalize dates/text)
  ↓
data/processed/clean_articles.json (28 clean articles)
  ↓
DEDUPLICATE (rapidfuzz, 90% threshold)
  ↓
data/processed/unique_articles.json (25 unique articles)
  ↓
ANALYZE (Gemini: summary, category, importance, keywords)
  ↓
data/processed/analyzed_articles.json (25 analyzed articles)
  ↓
STORE (JSON backup + Google Sheets)
  ↓
DETECT THEMES (Gemini: themes, trends, insights)
  ↓
data/processed/themes.json
  ↓
GENERATE DIGEST (MarkdownGenerator + PDFGenerator)
  ↓
data/reports/weekly_digest.md + weekly_digest.pdf
```

---

## 🔑 Key Technologies

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Core** | Python 3.12 | Backend |
| **AI** | Gemini API | Analysis, themes, insights |
| **Data Collection** | feedparser | RSS feeds |
| | requests | HTTP |
| | BeautifulSoup4 | HTML parsing |
| **Processing** | pandas | Data manipulation |
| | rapidfuzz | Duplicate detection |
| **Storage** | JSON | Backup |
| | Google Sheets API | Queryable storage |
| **Output** | Markdown | Digest format |
| | ReportLab | PDF generation |

---

## 📋 Complete File Structure

```
newsletter-research-agent/
│
├── README.md                        # Project documentation
├── requirements.txt                 # Dependencies
├── .gitignore                       # Git ignore rules
├── .env                             # API keys (not committed)
├── main.py                          # CLI Entry point
├── app.py                           # ⭐ Streamlit Web UI
├── IMPLEMENTATION_BLUEPRINT.md      # This blueprint
│
├── config/                          # Configuration
│   ├── settings.py                  # General settings
│   ├── sources.py                   # Source list
│   ├── categories.py                # Category definitions
│   └── prompts.py                   # Gemini prompts
│
├── src/                             # Source code
│   ├── agents/                      # Agent coordinators
│   │   ├── research_agent.py        # Main orchestrator
│   │   ├── collector_agent.py       # Collection coordinator
│   │   ├── analyzer_agent.py        # Analysis coordinator
│   │   ├── storage_agent.py         # Storage coordinator
│   │   ├── theme_agent.py           # Theme coordinator
│   │   └── digest_agent.py          # Digest coordinator
│   │
│   ├── collectors/                  # Data collectors
│   │   ├── rss_collector.py         # RSS feeds
│   │   ├── blog_collector.py        # Blog scraper
│   │   └── producthunt_collector.py # Product Hunt
│   │
│   ├── preprocessing/               # Data cleaning
│   │   ├── cleaner.py               # HTML/text cleaning
│   │   ├── validator.py             # Validation
│   │   └── normalizer.py            # Normalization
│   │
│   ├── duplicate/                   # Duplicate detection
│   │   ├── similarity.py            # Similarity calc
│   │   └── duplicate_checker.py     # Deduplication
│   │
│   ├── ai/                          # AI components
│   │   ├── gemini_client.py         # Gemini API wrapper
│   │   ├── analyzer.py              # Article analysis
│   │   ├── theme_detector.py        # Theme detection
│   │   └── digest_generator.py      # Digest generation
│   │
│   ├── storage/                     # Storage
│   │   ├── json_storage.py          # JSON operations
│   │   └── google_sheet.py          # Google Sheets
│   │
│   └── utils/                       # Utilities
│       ├── logger.py                # Logging
│       ├── helper.py                # Helpers
│       └── statistics.py            # Stats calculation
│
├── data/                            # Data storage
│   ├── raw/                         # Raw collected data
│   │   └── articles.json
│   ├── processed/                   # Processed data
│   │   ├── clean_articles.json
│   │   ├── unique_articles.json
│   │   ├── analyzed_articles.json
│   │   └── themes.json
│   └── reports/                     # Generated reports
│       ├── weekly_digest.md
│       └── weekly_digest.pdf
│
├── docs/                            # Documentation
│   ├── 01_Project_Overview.md
│   ├── 02_System_Architecture.md
│   ├── 03_Data_Models.md
│   ├── 04_API_Design.md
│   ├── 05_Module_Design.md
│   ├── 06_Class_Diagrams.md
│   ├── 07_Function_Specifications.md
│   ├── 08_Data_Flow.md
│   ├── 09_Prompt_Design.md
│   ├── 10_Error_Handling.md
│   ├── 11_Test_Plan.md
│   ├── 12_Deployment_Guide.md
│   ├── Builder_Note.pdf
│   ├── Architecture.png
│   └── Workflow.png
│
├── sample_output/                   # Sample outputs
│   ├── sample_sheet.csv
│   ├── weekly_digest.pdf
│   └── weekly_digest.md
│
├── logs/                            # Execution logs
│   └── research_agent_YYYYMMDD.log
│
└── tests/                           # Tests (optional)
    ├── test_collector.py
    ├── test_preprocessing.py
    ├── test_ai.py
    └── test_storage.py
```

---

## 🎓 Core Data Models

### RawArticle (Phase 3 output)
```python
{
    "title": str,
    "url": str,
    "source": str,
    "published": str,    # Any format
    "content": str       # May contain HTML
}
```

### CleanArticle (Phase 4 output)
```python
{
    "title": str,        # Trimmed
    "url": str,
    "source": str,
    "published": str,    # YYYY-MM-DD
    "content": str       # Plain text, no HTML
}
```

### AnalyzedArticle (Phase 6 output)
```python
{
    "title": str,
    "url": str,
    "source": str,
    "published": str,
    "summary": str,                # Gemini summary
    "category": str,               # Model Release, Funding, etc.
    "importance": str,             # High, Medium, Low
    "companies": list[str],        # ["OpenAI", "Anthropic"]
    "products": list[str],         # ["GPT-5", "Claude"]
    "keywords": list[str],         # ["Reasoning", "Coding"]
    "funding": dict | None,        # {"amount": "30M", "stage": "Series A"}
    "tags": list[str]              # ["AI", "Model"]
}
```

### WeeklyThemes (Phase 8 output)
```python
{
    "top_themes": list[str],              # ["AI Agents", "Reasoning"]
    "key_insights": list[str],            # Narrative insights
    "most_mentioned_companies": list[str],
    "trending_topics": list[str],
    "important_events": list[str]
}
```

---

## ⚙️ Key Configuration

### .env
```bash
GEMINI_API_KEY=your_key_here
GOOGLE_SHEET_ID=optional_sheet_id
```

### config/sources.py
```python
SOURCES = [
    {"name": "OpenAI", "type": "blog", "url": "...", "enabled": True},
    {"name": "Anthropic", "type": "blog", "url": "...", "enabled": True},
    {"name": "Hugging Face", "type": "blog", "url": "...", "enabled": True},
    {"name": "TechCrunch AI", "type": "blog", "url": "...", "enabled": True},
    {"name": "Product Hunt", "type": "product_hunt", "url": "...", "enabled": True},
]
```

### config/categories.py
```python
CATEGORIES = [
    "Model Release",
    "Funding",
    "Research",
    "Product Launch",
    "Tool Update",
    "Open Source",
    "Enterprise AI",
    "Benchmark",
    "Acquisition",
    "Startup"
]
```

---

## 🚀 Quick Start Commands

```bash
# 1. Setup
git clone <repo>
cd newsletter-research-agent
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Configure
cp .env.example .env
# Add GEMINI_API_KEY to .env

# 3. Run
python main.py

# 4. Output
# Check: data/reports/weekly_digest.pdf
```

---

## ⏱️ Expected Timeline

### Day 1 Morning (3 hours)
- ✅ Phase 1: Setup (30 min)
- ✅ Phase 2: Configuration (30 min)
- ✅ Phase 3: Collection (2 hours)

### Day 1 Afternoon (4 hours)
- ✅ Phase 4: Preprocessing (1.5 hours)
- ✅ Phase 5: Duplicate Detection (1 hour)
- ✅ Phase 6: Start AI Analysis (1.5 hours)

### Day 1 Evening (2 hours)
- ✅ Phase 6: Complete AI Analysis (2 hours)

### Day 2 Morning (4 hours)
- ✅ Phase 7: Storage (1.5 hours)
- ✅ Phase 8: Theme Detection (2 hours)
- ✅ Integration Testing (30 min)

### Day 2 Afternoon (4 hours)
- ✅ Phase 9: Digest Generation (2 hours)
- ✅ Phase 10: Documentation (1.5 hours)
- ✅ Final Testing & Sample Outputs (30 min)

**Total**: ~17 hours over 2 days

---

## ✅ Assignment Requirements Coverage

| Requirement | Implementation | Status |
|-------------|----------------|--------|
| Monitor 5+ sources | config/sources.py with 5+ entries | ✅ |
| Collect updates | CollectorAgent (RSS + scraping) | ✅ |
| Extract insights | Gemini analysis (Phase 6) | ✅ |
| Categorize | Gemini categorization | ✅ |
| Store in queryable destination | Google Sheets + JSON | ✅ |
| Generate weekly digest | DigestAgent (MD + PDF) | ✅ |
| Linked source references | URLs in all outputs | ✅ |
| Builder's Note | docs/Builder_Note.pdf | ✅ |

---

## 🎯 Success Criteria

### Functional
- [ ] Collects articles from 5+ sources
- [ ] Removes duplicates effectively
- [ ] Gemini analysis produces quality summaries
- [ ] Google Sheets populated correctly
- [ ] Themes detected accurately
- [ ] PDF newsletter looks professional

### Technical
- [ ] No hardcoded API keys
- [ ] Error handling works gracefully
- [ ] Logging configured properly
- [ ] Code organized and modular
- [ ] Documentation complete

### Deliverables
- [ ] GitHub repository with clean code
- [ ] README with clear instructions
- [ ] Builder's Note (1 page)
- [ ] Sample weekly digest PDF
- [ ] Google Sheets link (if configured)

---

## 📚 Blueprint Documents Index

1. **01_Project_Overview.md** - What & Why
2. **02_System_Architecture.md** - High-level design
3. **03_Data_Models.md** - Data structures
4. **04_API_Design.md** - External APIs
5. **05_Module_Design.md** - File organization
6. **06_Class_Diagrams.md** - OOP design
7. **07_Function_Specifications.md** - Function details
8. **08_Data_Flow.md** - Pipeline flow
9. **09_Prompt_Design.md** - AI prompts
10. **10_Error_Handling.md** - Error strategy
11. **11_Test_Plan.md** - Testing approach
12. **12_Deployment_Guide.md** - Setup & run

---

## 🔥 Ready to Build!

You have:
- ✅ Complete architecture designed
- ✅ All data models defined
- ✅ Every function specified
- ✅ Error handling planned
- ✅ Testing strategy ready
- ✅ Deployment guide prepared

**Next Step**: Begin implementation with Phase 1 (Setup)

**Good luck! ⚔️🔥**
