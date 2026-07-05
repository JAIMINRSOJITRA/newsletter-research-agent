# Implementation Checklist - AI Research Agent

Use this checklist to track your progress through all 10 phases.

---

## 🎯 PHASE 1: Project Setup

### Folder Structure
- [ ] Create main project folder `newsletter-research-agent/`
- [ ] Create `config/` folder
- [ ] Create `src/` folder with subfolders:
  - [ ] `src/agents/`
  - [ ] `src/collectors/`
  - [ ] `src/preprocessing/`
  - [ ] `src/duplicate/`
  - [ ] `src/ai/`
  - [ ] `src/storage/`
  - [ ] `src/utils/`
- [ ] Create `data/` folder with subfolders:
  - [ ] `data/raw/`
  - [ ] `data/processed/`
  - [ ] `data/reports/`
- [ ] Create `docs/` folder
- [ ] Create `sample_output/` folder
- [ ] Create `logs/` folder
- [ ] Create `tests/` folder

### Git Setup
- [ ] Initialize Git repository (`git init`)
- [ ] Create `.gitignore` file
- [ ] Add to .gitignore:
  - [ ] `.venv/`
  - [ ] `.env`
  - [ ] `__pycache__/`
  - [ ] `*.pyc`
  - [ ] `*.log`
  - [ ] `credentials.json`
- [ ] Initial commit

### Virtual Environment
- [ ] Create virtual environment (`python -m venv .venv`)
- [ ] Activate virtual environment
- [ ] Verify Python version (3.12+)

### Dependencies
- [ ] Create `requirements.txt` with all packages
- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] Verify installations work:
  - [ ] `import google.generativeai`
  - [ ] `import feedparser`
  - [ ] `import requests`
  - [ ] `import bs4`
  - [ ] `import pandas`
  - [ ] `import rapidfuzz`

### Environment File
- [ ] Create `.env` file
- [ ] Add `GEMINI_API_KEY=` placeholder
- [ ] Get Gemini API key from https://aistudio.google.com/app/apikey
- [ ] Add actual API key to `.env`
- [ ] Test API key works

### `__init__.py` Files
- [ ] Create `config/__init__.py`
- [ ] Create `src/__init__.py`
- [ ] Create `src/agents/__init__.py`
- [ ] Create `src/collectors/__init__.py`
- [ ] Create `src/preprocessing/__init__.py`
- [ ] Create `src/duplicate/__init__.py`
- [ ] Create `src/ai/__init__.py`
- [ ] Create `src/storage/__init__.py`
- [ ] Create `src/utils/__init__.py`
- [ ] Create `tests/__init__.py`

**Phase 1 Complete**: ✅ Project structure ready for coding

---

## 🎯 PHASE 2: Configuration

### config/settings.py
- [ ] Create file
- [ ] Import `os`, `dotenv`
- [ ] Load environment variables
- [ ] Define:
  - [ ] `GEMINI_API_KEY`
  - [ ] `GEMINI_MODEL`
  - [ ] `DUPLICATE_THRESHOLD`
  - [ ] `GEMINI_DELAY_SECONDS`
  - [ ] File paths (DATA_DIR, RAW_DIR, etc.)
  - [ ] Logging configuration
- [ ] Test: Can import and access settings

### config/sources.py
- [ ] Create file
- [ ] Define `SOURCES` list with 5+ sources:
  - [ ] OpenAI
  - [ ] Anthropic
  - [ ] Hugging Face
  - [ ] TechCrunch AI
  - [ ] Product Hunt
- [ ] Each source has: name, type, url, enabled
- [ ] Test: Can import `SOURCES`

### config/categories.py
- [ ] Create file
- [ ] Define `CATEGORIES` list with:
  - [ ] Model Release
  - [ ] Funding
  - [ ] Research
  - [ ] Product Launch
  - [ ] Tool Update
  - [ ] Open Source
  - [ ] Enterprise AI
  - [ ] Benchmark
  - [ ] Acquisition
  - [ ] Startup
- [ ] Define `IMPORTANCE_LEVELS = ["High", "Medium", "Low"]`
- [ ] Test: Can import categories

### config/prompts.py
- [ ] Create file
- [ ] Define `ARTICLE_ANALYSIS_PROMPT` (from docs/09)
- [ ] Define `THEME_DETECTION_PROMPT` (from docs/09)
- [ ] Define `DIGEST_GENERATION_PROMPT` (optional, from docs/09)
- [ ] Test: Can import prompts

**Phase 2 Complete**: ✅ All configurations defined

---

## 🎯 PHASE 3: Collection

### src/collectors/rss_collector.py
- [ ] Create `RSSCollector` class
- [ ] Implement `collect(source)` method
- [ ] Implement `parse_feed(url)` method
- [ ] Implement `extract_article(entry)` method
- [ ] Test with OpenAI RSS feed

### src/collectors/blog_collector.py
- [ ] Create `BlogCollector` class
- [ ] Implement `collect(source)` method
- [ ] Implement `fetch_page(url)` method
- [ ] Implement `extract_articles(html, source)` method
- [ ] Test with Anthropic blog

### src/collectors/producthunt_collector.py
- [ ] Create `ProductHuntCollector` class
- [ ] Implement `collect(source)` method
- [ ] Implement `extract_products(html)` method
- [ ] Test with Product Hunt

### src/agents/collector_agent.py
- [ ] Create `CollectorAgent` class
- [ ] Implement `collect_all()` method
- [ ] Implement `collect_from_source(source)` method
- [ ] Implement `normalize_articles(articles)` method
- [ ] Implement `save_raw(articles)` method
- [ ] Test: Collects from all enabled sources

### Testing Phase 3
- [ ] Run collector independently
- [ ] Verify `data/raw/articles.json` created
- [ ] Check article count (should be 20+)
- [ ] Verify each article has: title, url, source, content
- [ ] Check for errors in console

**Phase 3 Complete**: ✅ Articles collected and saved

---

## 🎯 PHASE 4: Preprocessing

### src/preprocessing/validator.py
- [ ] Create `Validator` class
- [ ] Implement `validate_article(article)` method
- [ ] Check required fields exist
- [ ] Check content length >= 100
- [ ] Test with valid and invalid articles

### src/preprocessing/cleaner.py
- [ ] Create `Cleaner` class
- [ ] Implement `clean_html(text)` method (BeautifulSoup)
- [ ] Implement `normalize_text(text)` method
- [ ] Implement `normalize_whitespace(text)` method
- [ ] Test: HTML removed, text cleaned

### src/preprocessing/normalizer.py
- [ ] Create `Normalizer` class
- [ ] Implement `normalize_date(date_str)` method
- [ ] Support multiple date formats
- [ ] Return YYYY-MM-DD format
- [ ] Test with various date formats

### src/preprocessing/preprocessor.py
- [ ] Create `Preprocessor` class
- [ ] Implement `process(articles)` method
- [ ] Integrate validator, cleaner, normalizer
- [ ] Filter invalid articles
- [ ] Test: Raw articles → clean articles

### Testing Phase 4
- [ ] Run preprocessor on raw articles
- [ ] Verify `data/processed/clean_articles.json` created
- [ ] Check HTML removed
- [ ] Verify dates in YYYY-MM-DD format
- [ ] Confirm invalid articles removed

**Phase 4 Complete**: ✅ Articles cleaned and validated

---

## 🎯 PHASE 5: Duplicate Detection

### src/duplicate/similarity.py
- [ ] Create `SimilarityCalculator` class
- [ ] Implement `calculate_similarity(title1, title2)` method
- [ ] Use rapidfuzz.fuzz.ratio()
- [ ] Return score 0-100
- [ ] Test with similar and different titles

### src/duplicate/duplicate_checker.py
- [ ] Create `DuplicateChecker` class
- [ ] Implement `remove_duplicates(articles)` method
- [ ] Implement `is_duplicate(article1, article2)` method
- [ ] Implement `find_duplicates(articles)` method
- [ ] Use threshold from settings (90%)
- [ ] Return (unique, duplicates) tuple
- [ ] Test: Detects and removes duplicates

### Testing Phase 5
- [ ] Run duplicate checker
- [ ] Verify `data/processed/unique_articles.json` created
- [ ] Verify `data/processed/duplicates.json` created (optional)
- [ ] Check duplicate count makes sense
- [ ] Manually verify a few duplicates are actually similar

**Phase 5 Complete**: ✅ Duplicates removed

---

## 🎯 PHASE 6: AI Analysis

### src/ai/gemini_client.py
- [ ] Create `GeminiClient` class
- [ ] Implement `__init__(api_key, model)` method
- [ ] Implement `configure()` method
- [ ] Implement `generate(prompt, response_type)` method
- [ ] Implement `generate_with_retry(prompt, max_retries)` method
- [ ] Handle rate limiting with exponential backoff
- [ ] Test: Can generate responses

### src/ai/analyzer.py
- [ ] Create `ArticleAnalyzer` class
- [ ] Implement `analyze(article)` method
- [ ] Implement `build_prompt(article)` method
- [ ] Implement `parse_response(response)` method
- [ ] Use `ARTICLE_ANALYSIS_PROMPT` from config
- [ ] Test: Returns structured JSON

### src/agents/analyzer_agent.py
- [ ] Create `AnalyzerAgent` class
- [ ] Implement `analyze_all(articles)` method
- [ ] Implement `analyze_article(article)` method
- [ ] Add 4-second delay between requests
- [ ] Log progress (1/20, 2/20, etc.)
- [ ] Test: Analyzes all articles

### Testing Phase 6
- [ ] Run analyzer with a few articles first
- [ ] Verify API key works
- [ ] Check JSON response structure
- [ ] Run full analysis
- [ ] Verify `data/processed/analyzed_articles.json` created
- [ ] Check each article has: summary, category, importance, companies, products, keywords
- [ ] Verify quality of summaries
- [ ] Confirm categories are valid

**Phase 6 Complete**: ✅ Articles analyzed with Gemini

---

## 🎯 PHASE 7: Storage

### src/storage/json_storage.py
- [ ] Create `JSONStorage` class
- [ ] Implement `save(data, filepath)` method
- [ ] Implement `load(filepath)` method
- [ ] Implement `append(data, filepath)` method
- [ ] Test: Can save and load JSON

### src/storage/google_sheet.py (Optional)
- [ ] Create `GoogleSheetStorage` class
- [ ] Implement `authenticate()` method
- [ ] Implement `open_sheet(sheet_id)` method
- [ ] Implement `append_rows(rows)` method
- [ ] Implement `read_all()` method
- [ ] Get credentials.json
- [ ] Create/share Google Sheet
- [ ] Test: Can authenticate and write

### src/agents/storage_agent.py
- [ ] Create `StorageAgent` class
- [ ] Implement `save_all(articles)` method
- [ ] Implement `save_to_json(articles, filepath)` method
- [ ] Implement `save_to_sheets(articles)` method (optional)
- [ ] Always save JSON first
- [ ] Handle Google Sheets errors gracefully
- [ ] Test: Saves to both destinations

### Testing Phase 7
- [ ] Run storage agent
- [ ] Verify JSON backup saved
- [ ] If using Google Sheets:
  - [ ] Verify authentication works
  - [ ] Check rows appended correctly
  - [ ] Verify all columns populated
  - [ ] Test filtering/sorting in Sheets

**Phase 7 Complete**: ✅ Data stored in queryable format

---

## 🎯 PHASE 8: Theme Detection

### src/utils/statistics.py
- [ ] Create `StatisticsCalculator` class
- [ ] Implement `calculate(articles)` method
- [ ] Implement `count_by_category(articles)` method
- [ ] Implement `count_company_mentions(articles)` method
- [ ] Implement `count_product_mentions(articles)` method
- [ ] Implement `get_date_range(articles)` method
- [ ] Test: Calculates all stats correctly

### src/ai/theme_detector.py
- [ ] Create `ThemeDetector` class
- [ ] Implement `detect(summaries)` method
- [ ] Implement `build_prompt(summaries)` method
- [ ] Implement `parse_response(response)` method
- [ ] Use `THEME_DETECTION_PROMPT` from config
- [ ] Test: Returns themes structure

### src/agents/theme_agent.py
- [ ] Create `ThemeAgent` class
- [ ] Implement `detect_themes(articles)` method
- [ ] Implement `extract_summaries(articles)` method
- [ ] Combine Gemini themes + Python statistics
- [ ] Save to `themes.json`
- [ ] Test: Themes + stats generated

### Testing Phase 8
- [ ] Run theme agent
- [ ] Verify `data/processed/themes.json` created
- [ ] Check themes make sense for articles
- [ ] Verify insights are relevant
- [ ] Confirm statistics are accurate
- [ ] Check company/product mentions

**Phase 8 Complete**: ✅ Weekly themes detected

---

## 🎯 PHASE 9: Digest Generation

### src/digest/markdown_generator.py
- [ ] Create `MarkdownGenerator` class
- [ ] Implement `generate(articles, themes, stats)` method
- [ ] Implement `generate_header(stats)` method
- [ ] Implement `generate_themes_section(themes)` method
- [ ] Implement `generate_category_section(category, articles)` method
- [ ] Implement `generate_statistics_section(stats)` method
- [ ] Implement `generate_sources_section(articles)` method
- [ ] Test: Generates proper markdown

### src/digest/pdf_generator.py
- [ ] Create `PDFGenerator` class
- [ ] Implement `generate(md_filepath, pdf_filepath)` method
- [ ] Implement `markdown_to_pdf(md_content)` method
- [ ] Use ReportLab or markdown library
- [ ] Test: Creates readable PDF

### src/agents/digest_agent.py
- [ ] Create `DigestAgent` class
- [ ] Implement `generate_digest(articles, themes)` method
- [ ] Implement `generate_markdown(articles, themes)` method
- [ ] Implement `save_markdown(content, filepath)` method
- [ ] Implement `generate_pdf(md_path, pdf_path)` method
- [ ] Test: Full digest generation works

### Testing Phase 9
- [ ] Run digest agent
- [ ] Verify `data/reports/weekly_digest.md` created
- [ ] Verify `data/reports/weekly_digest.pdf` created
- [ ] Open PDF and check:
  - [ ] Professional appearance
  - [ ] All sections present
  - [ ] No formatting errors
  - [ ] Links work
  - [ ] Information accurate

**Phase 9 Complete**: ✅ Weekly newsletter generated

---

## 🎯 PHASE 10: Web UI (Streamlit) ⭐ BONUS

### app.py (Main UI File)
- [ ] Create `app.py` in root directory
- [ ] Import Streamlit and required modules
- [ ] Configure page (title, icon, layout)
- [ ] Create sidebar navigation
- [ ] Route to different pages

### Home Page
- [ ] Display project title and description
- [ ] Show metrics cards (articles, sources, last run)
- [ ] Display recent activity
- [ ] Add quick action buttons

### Configuration Page
- [ ] API key input (password field)
- [ ] Source list with enable/disable toggles
- [ ] Settings sliders (duplicate threshold, etc.)
- [ ] Model selection dropdown
- [ ] Save configuration button
- [ ] Test connection button

### Run Pipeline Page
- [ ] Start/Stop buttons
- [ ] Progress bar for each phase
- [ ] Real-time status updates (✓/⏳/❌)
- [ ] Live log streaming
- [ ] Success/error notifications

### Analytics Page
- [ ] Load analyzed articles
- [ ] Bar chart: Articles by category (plotly)
- [ ] List: Top companies mentioned
- [ ] Pie chart: Importance distribution
- [ ] Export CSV button

### View Digest Page
- [ ] Download PDF button
- [ ] Download Markdown button
- [ ] Markdown preview
- [ ] List previous digests

### Styling
- [ ] Add custom CSS (optional)
- [ ] Use columns for layout
- [ ] Add icons to improve visuals
- [ ] Ensure responsive design

### Testing UI
- [ ] Run `streamlit run app.py`
- [ ] Test all navigation
- [ ] Test configuration save/load
- [ ] Test pipeline execution from UI
- [ ] Verify analytics charts display
- [ ] Check digest preview works
- [ ] Test on different screen sizes

### Dependencies
- [ ] Add `streamlit==1.32.0` to requirements.txt
- [ ] Add `plotly==5.18.0` to requirements.txt
- [ ] Reinstall: `pip install -r requirements.txt`

**Phase 10 Complete**: ✅ Professional Web UI ready

---

## 🎯 PHASE 11: Documentation

### README.md
- [ ] Project description
- [ ] Features list
- [ ] Tech stack table
- [ ] Installation instructions
- [ ] Configuration guide
- [ ] How to run
- [ ] Folder structure
- [ ] Sample output references
- [ ] Future improvements
- [ ] License (optional)

### docs/Builder_Note.pdf
- [ ] Project overview (1-2 paragraphs)
- [ ] Tool stack table
- [ ] Workflow diagram
- [ ] Folder structure
- [ ] **Screenshot of UI** ⭐
- [ ] How content team uses it (via UI!)
- [ ] Future improvements
- [ ] Keep to 1 page
- [ ] Export as PDF

### Architecture Diagrams
- [ ] Create workflow diagram (draw.io or similar)
- [ ] Export as `docs/Workflow.png`
- [ ] Create architecture diagram
- [ ] Export as `docs/Architecture.png`

### sample_output/
- [ ] Copy `weekly_digest.md` to `sample_output/`
- [ ] Copy `weekly_digest.pdf` to `sample_output/`
- [ ] Export Google Sheets as CSV → `sample_sheet.csv` (optional)

### Code Documentation
- [ ] Add docstrings to main classes
- [ ] Add comments for complex logic
- [ ] Review and clean up any debug code
- [ ] Remove unused imports

**Phase 10 Complete**: ✅ Project fully documented

---

## 🎯 INTEGRATION & TESTING

### main.py
- [ ] Create entry point file
- [ ] Import `ResearchAgent`
- [ ] Implement basic CLI (optional)
- [ ] Add execution logging
- [ ] Test: Can run full pipeline

### Full Pipeline Test
- [ ] Delete all `data/` output files
- [ ] Run `python main.py`
- [ ] Watch for errors
- [ ] Verify all phases complete
- [ ] Check all output files created
- [ ] Review final PDF quality

### Error Testing
- [ ] Test with invalid source URL
- [ ] Test with missing API key
- [ ] Test with Google Sheets unavailable
- [ ] Verify pipeline continues on non-critical errors

### Performance Check
- [ ] Note total execution time (should be 3-5 minutes)
- [ ] Check memory usage (should be < 1GB)
- [ ] Verify rate limiting works (4s delays)

**Integration Complete**: ✅ Full pipeline works end-to-end

---

## 🎯 PRE-SUBMISSION

### Code Quality
- [ ] No hardcoded API keys in code
- [ ] All sensitive data in .env
- [ ] No debug print() statements (use logger)
- [ ] Code formatted consistently
- [ ] Unused imports removed
- [ ] Comments for complex sections

### Git Repository
- [ ] .gitignore configured correctly
- [ ] .env NOT committed
- [ ] credentials.json NOT committed
- [ ] Clean commit history
- [ ] All files committed

### Documentation Check
- [ ] README.md complete and accurate
- [ ] Builder's Note PDF created
- [ ] Architecture diagrams created
- [ ] All docs/ files present
- [ ] sample_output/ folder populated

### Output Quality
- [ ] PDF looks professional
- [ ] No formatting errors
- [ ] Links work
- [ ] Information accurate
- [ ] Sources listed

### Requirements Coverage
- [ ] ✅ Monitors 5+ sources
- [ ] ✅ Collects updates automatically
- [ ] ✅ Extracts insights with AI
- [ ] ✅ Categorizes information
- [ ] ✅ Stores in queryable destination
- [ ] ✅ Generates weekly digest
- [ ] ✅ Includes source references
- [ ] ✅ Builder's Note included

### Final Checks
- [ ] requirements.txt up to date
- [ ] Virtual environment deactivated for submission
- [ ] All files in correct folders
- [ ] No unnecessary files included
- [ ] Repository size reasonable (< 50MB)

**Pre-Submission Complete**: ✅ Ready to submit

---

## 🎯 SUBMISSION PACKAGE

### GitHub Repository
- [ ] Repository created on GitHub
- [ ] All code pushed
- [ ] README visible on homepage
- [ ] .gitignore working (no .env, .venv in repo)

### Deliverables
- [ ] GitHub repository link
- [ ] `data/reports/weekly_digest.pdf`
- [ ] `docs/Builder_Note.pdf`
- [ ] Google Sheets link (if used)
- [ ] README.md (in repository)

### Optional Extras
- [ ] Video demo (< 3 minutes)
- [ ] Deployed version (Streamlit/Heroku)
- [ ] Additional documentation

**Submission Package Complete**: ✅ Ready to submit at 2 PM!

---

## 📊 Progress Tracker

| Phase | Status | Time Spent | Notes |
|-------|--------|------------|-------|
| 1. Setup | ⬜ | | |
| 2. Configuration | ⬜ | | |
| 3. Collection | ⬜ | | |
| 4. Preprocessing | ⬜ | | |
| 5. Duplicate Detection | ⬜ | | |
| 6. AI Analysis | ⬜ | | |
| 7. Storage | ⬜ | | |
| 8. Theme Detection | ⬜ | | |
| 9. Digest Generation | ⬜ | | |
| 10. Web UI (Streamlit) | ⬜ | | ⭐ |
| 11. Documentation | ⬜ | | |
| Integration Testing | ⬜ | | |
| Pre-Submission | ⬜ | | |

**Legend**: ⬜ Not Started | 🟨 In Progress | ✅ Complete

---

## 🎯 Emergency Shortcuts

If running out of time, prioritize in this order:

### Must Have (Core Functionality)
1. ✅ Phases 1-6 (Setup → AI Analysis)
2. ✅ Phase 7 (JSON storage only, skip Google Sheets)
3. ✅ Phase 9 (Digest generation)
4. ✅ Basic README

### Should Have
5. ✅ Phase 8 (Theme detection)
6. ✅ Phase 7 (Google Sheets)
7. ✅ Builder's Note

### Nice to Have
8. ⏭️ Architecture diagrams
9. ⏭️ Unit tests
10. ⏭️ Advanced error handling

---

**Good luck! Follow this checklist step by step. 🔥⚔️**
