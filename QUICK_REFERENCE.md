# Quick Reference Card - AI Research Agent

## 🎯 One-Page Cheat Sheet

### Project Summary
**Goal**: Automate AI newsletter generation from multiple sources
**Timeline**: 2 days
**Tech**: Python 3.12 + Gemini API
**Output**: Weekly digest (Markdown + PDF)

---

## 📦 Installation (5 minutes)

```bash
# Clone & setup
git clone <repo>
cd newsletter-research-agent
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Configure
echo "GEMINI_API_KEY=your_key_here" > .env

# Run
python main.py
```

---

## 📂 Critical Files

| File | Purpose |
|------|---------|
| `main.py` | Entry point |
| `config/sources.py` | Source list (5+) |
| `config/prompts.py` | Gemini prompts |
| `.env` | API keys (NEVER commit) |
| `data/reports/weekly_digest.pdf` | Final output |

---

## 🔄 10 Phases at a Glance

```
1. Setup       → Folders + Git + Venv
2. Config      → sources.py (5+ sources)
3. Collect     → RSS + Scraping → raw/articles.json
4. Preprocess  → Clean + Validate → clean_articles.json
5. Dedupe      → rapidfuzz 90% → unique_articles.json
6. Analyze     → Gemini → analyzed_articles.json
7. Store       → JSON + Google Sheets
8. Themes      → Gemini + Stats → themes.json
9. Digest      → MD + PDF → weekly_digest.pdf
10. Docs       → README + Builder's Note
```

---

## 🏗️ Key Components

### Main Classes
- `ResearchAgent` - Orchestrator
- `CollectorAgent` - Gathers articles
- `AnalyzerAgent` - Gemini analysis
- `StorageAgent` - Saves data
- `ThemeAgent` - Detects themes
- `DigestAgent` - Generates newsletter

### Data Models
- `RawArticle` - After collection
- `CleanArticle` - After preprocessing
- `AnalyzedArticle` - After Gemini (has summary, category, etc.)
- `WeeklyThemes` - After theme detection

---

## 🔧 Configuration Quick Reference

### config/sources.py
```python
SOURCES = [
    {"name": "OpenAI", "type": "blog", "url": "...", "enabled": True},
    # Add 4+ more
]
```

### config/prompts.py
```python
ARTICLE_ANALYSIS_PROMPT = """
You are an AI newsletter researcher...
Return ONLY valid JSON...
"""
```

### config/settings.py
```python
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-1.5-flash"
DUPLICATE_THRESHOLD = 90.0
GEMINI_DELAY_SECONDS = 4
```

---

## 🎨 AnalyzedArticle Structure

```python
{
    "title": str,
    "url": str,
    "source": str,
    "published": "YYYY-MM-DD",
    "summary": str,                    # Gemini
    "category": str,                   # Model Release, Funding, etc.
    "importance": str,                 # High, Medium, Low
    "companies": ["OpenAI", "..."],
    "products": ["GPT-5", "..."],
    "keywords": ["Reasoning", "..."],
    "funding": {"amount": "30M", "stage": "Series A"} | None,
    "tags": ["AI", "Model", "..."]
}
```

---

## ⚙️ Common Commands

```bash
# Activate environment
source .venv/bin/activate           # Mac/Linux
.venv\Scripts\activate              # Windows

# Run CLI pipeline
python main.py

# Run Web UI ⭐
streamlit run app.py

# Check logs
tail -f logs/research_agent_*.log

# Test single phase
python -c "from src.agents.collector_agent import CollectorAgent; CollectorAgent().collect_all()"

# Deactivate environment
deactivate
```

---

## 🐛 Quick Troubleshooting

| Error | Solution |
|-------|----------|
| `Invalid API key` | Check .env file, ensure GEMINI_API_KEY is set |
| `No articles collected` | Check source URLs, internet connection |
| `Rate limit exceeded` | Increase GEMINI_DELAY_SECONDS to 5 |
| `Google Sheets auth failed` | Check credentials.json, or disable sheets |
| `Module not found` | Run `pip install -r requirements.txt` |

---

## 📊 Expected Performance

| Metric | Value |
|--------|-------|
| Articles collected | 20-30 |
| Processing time | 3-5 minutes |
| Gemini API calls | 25-30 |
| Output size | ~1 MB |
| Success rate | >95% |

---

## ✅ Pre-Submission Checklist

```
Code
  [ ] No hardcoded API keys
  [ ] .env in .gitignore
  [ ] All imports used
  [ ] Logging (not print)

Outputs
  [ ] data/reports/weekly_digest.pdf exists
  [ ] sample_output/ folder populated
  [ ] Google Sheets link works (if used)

Documentation
  [ ] README.md complete
  [ ] Builder's Note PDF created
  [ ] Comments for complex logic

Testing
  [ ] Full pipeline runs successfully
  [ ] Output quality verified
  [ ] All phases tested individually
```

---

## 📚 Blueprint Documents

| Doc | Purpose | When to Read |
|-----|---------|--------------|
| 01_Project_Overview | What & Why | Start |
| 02_System_Architecture | High-level design | Planning |
| 03_Data_Models | Data structures | Before coding |
| 04_API_Design | External APIs | API integration |
| 05_Module_Design | File organization | Start |
| 06_Class_Diagrams | OOP design | Before coding |
| 07_Function_Specifications | Function details | During coding |
| 08_Data_Flow | Pipeline flow | Understanding |
| 09_Prompt_Design | Gemini prompts | Phase 6, 8, 9 |
| 10_Error_Handling | Error strategy | During coding |
| 11_Test_Plan | Testing approach | Testing phase |
| 12_Deployment_Guide | Setup & run | Setup + Deployment |

---

## 🚀 2-Day Timeline

### Day 1
- **Morning**: Setup + Collection (Phases 1-3)
- **Afternoon**: Preprocessing + Dedupe (Phases 4-5)
- **Evening**: Start AI Analysis (Phase 6)

### Day 2
- **Morning**: Complete Analysis + Storage + Themes (Phases 6-8)
- **Afternoon**: Digest + Documentation (Phases 9-10)
- **Submit**: 2 PM

---

## 🎯 Assignment Requirements ✓

```
✅ Monitor 5+ sources       → config/sources.py
✅ Collect updates          → CollectorAgent
✅ Extract insights         → Gemini analysis
✅ Categorize information   → Gemini categorization
✅ Store queryable          → Google Sheets + JSON
✅ Generate digest          → weekly_digest.pdf
✅ Linked references        → URLs included
✅ Builder's Note           → docs/Builder_Note.pdf
```

---

## 💾 File Paths Quick Reference

```
# Input
config/sources.py           → Source configurations
.env                        → API keys

# Data (Pipeline)
data/raw/articles.json
data/processed/clean_articles.json
data/processed/unique_articles.json
data/processed/analyzed_articles.json
data/processed/themes.json

# Output
data/reports/weekly_digest.md
data/reports/weekly_digest.pdf    → Submit this!

# Logs
logs/research_agent_YYYYMMDD.log
```

---

## 🔑 Environment Variables

```bash
# .env file (NEVER commit this)
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
GOOGLE_SHEET_ID=your_sheet_id
GOOGLE_CREDENTIALS_PATH=credentials.json
```

---

## 🎨 Categories

```python
"Model Release"     # GPT-5, Claude 4
"Funding"           # Series A, acquisitions
"Research"          # Papers, studies
"Product Launch"    # New tools, apps
"Tool Update"       # Updates to existing
"Open Source"       # Open-source releases
"Enterprise AI"     # B2B, enterprise news
"Benchmark"         # Performance tests
"Acquisition"       # M&A
"Startup"           # New startups
```

---

## ⏱️ Rate Limits

| API | Limit | Our Strategy |
|-----|-------|--------------|
| Gemini Free | 15 req/min | 4s delay between calls |
| Google Sheets | 60 req/min | Batch operations |

---

## 🔥 Key Success Factors

1. **Read blueprint first** - Don't guess implementations
2. **Test each phase** - Before moving to next
3. **Handle errors gracefully** - Log and continue
4. **Use logger, not print** - Professional logging
5. **Git commits frequently** - Save progress
6. **Follow data models exactly** - Consistency matters

---

## 📖 Quick Code Snippets

### Run Full Pipeline
```python
from src.agents.research_agent import ResearchAgent

agent = ResearchAgent()
result = agent.run()
print(f"Success! Generated: {result['digest_path']}")
```

### Test Gemini Connection
```python
from src.ai.gemini_client import GeminiClient

client = GeminiClient()
response = client.generate("Say hello")
print(response)
```

### Load Analyzed Articles
```python
import json

with open('data/processed/analyzed_articles.json') as f:
    articles = json.load(f)
    
print(f"Loaded {len(articles)} articles")
```

---

## 🎓 What Reviewers Look For

✅ Clean architecture
✅ Modular code
✅ Error handling
✅ Professional output
✅ Complete documentation
✅ Working demo
✅ Clear commit history

---

## 🆘 Emergency Contacts

- **Blueprint**: `IMPLEMENTATION_BLUEPRINT.md`
- **Summary**: `BLUEPRINT_SUMMARY.md`
- **Architecture**: `docs/ARCHITECTURE_DIAGRAM.txt`
- **This File**: `QUICK_REFERENCE.md`

---

## 💡 Final Tips

1. **Gemini API Key**: Get from https://aistudio.google.com/app/apikey
2. **Test with 1 source first**: Enable only OpenAI initially
3. **Check logs**: `logs/` folder has all execution details
4. **Verify JSON files**: After each phase, check data/ folder
5. **Keep it simple**: Demo quality, not production quality

---

**Good luck! 🔥⚔️**

**Remember**: This is a demo. Focus on:
- ✅ Working features
- ✅ Clean structure
- ✅ Good documentation

NOT:
- ❌ Perfect error handling
- ❌ 100% test coverage
- ❌ Production optimization

---

**Questions?** Check:
1. `docs/12_Deployment_Guide.md` for setup issues
2. `docs/10_Error_Handling.md` for errors
3. `docs/11_Test_Plan.md` for testing
