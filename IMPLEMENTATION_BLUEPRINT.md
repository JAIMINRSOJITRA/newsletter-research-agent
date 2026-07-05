# AI Research Agent - Implementation Blueprint

## 📋 Overview

This document serves as the complete implementation guide for the AI Research Agent project. It contains all design decisions, specifications, and implementation details needed to build the system from scratch.

**Project Goal**: Automate AI news collection, analysis, and newsletter generation

**Timeline**: 2-day internship demo

**API**: Gemini API only (no OpenAI, Anthropic APIs)

---

## 📚 Blueprint Structure

This blueprint is organized into 12 comprehensive documents:

### 01 - Project Overview
**Location**: `docs/01_Project_Overview.md`

**Contains**:
- Problem statement
- Solution overview
- Key features
- Project scope
- Target users

**Purpose**: Understand what we're building and why

---

### 02 - System Architecture
**Location**: `docs/02_System_Architecture.md`

**Contains**:
- High-level architecture diagram
- Technology stack
- Agent architecture
- Data flow pipeline
- Component relationships

**Purpose**: Understand system structure and dependencies

---

### 03 - Data Models
**Location**: `docs/03_Data_Models.md`

**Contains**:
- All data structures (RawArticle, CleanArticle, AnalyzedArticle, etc.)
- JSON schemas
- Google Sheets schema
- Category definitions
- Importance levels

**Purpose**: Define exact structure of all data flowing through the system

---

### 04 - API Design
**Location**: `docs/04_API_Design.md`

**Contains**:
- Gemini API usage
- Google Sheets API usage
- RSS feed handling
- Web scraping approach
- Environment variables
- Rate limits & quotas

**Purpose**: Specify all external integrations

---

### 05 - Module Design
**Location**: `docs/05_Module_Design.md`

**Contains**:
- Complete folder structure
- Every Python file and its purpose
- Module responsibilities
- File dependencies

**Purpose**: Define project organization and module boundaries

---

### 06 - Class Diagrams
**Location**: `docs/06_Class_Diagrams.md`

**Contains**:
- All classes with methods and properties
- Class relationships
- Dependency graph
- Object interactions

**Purpose**: Define object-oriented design

---

### 07 - Function Specifications
**Location**: `docs/07_Function_Specifications.md`

**Contains**:
- Every function signature
- Input/output specifications
- Purpose and flow
- Error handling per function
- Dependencies

**Purpose**: Specify exactly what each function does before coding

---

### 08 - Data Flow
**Location**: `docs/08_Data_Flow.md`

**Contains**:
- Complete pipeline visualization
- Data transformation examples
- File dependencies
- Phase-by-phase flow

**Purpose**: Understand how data moves through the system

---

### 09 - Prompt Design
**Location**: `docs/09_Prompt_Design.md`

**Contains**:
- All Gemini prompts
- Prompt engineering best practices
- Expected outputs
- Test cases

**Purpose**: Define AI interactions and outputs

---

### 10 - Error Handling
**Location**: `docs/10_Error_Handling.md`

**Contains**:
- Error handling strategy
- Error categories
- Recovery strategies
- Logging configuration
- Default values

**Purpose**: Handle failures gracefully

---

### 11 - Test Plan
**Location**: `docs/11_Test_Plan.md`

**Contains**:
- Manual testing checklist
- Integration testing
- Sample data verification
- Performance expectations
- Pre-submission checklist

**Purpose**: Verify system works correctly

---

### 12 - Deployment Guide
**Location**: `docs/12_Deployment_Guide.md`

**Contains**:
- Installation instructions
- Configuration guide
- Running the agent
- Troubleshooting
- Maintenance guide

**Purpose**: Enable anyone to run the system

---

## 🎯 How to Use This Blueprint

### For Implementation

1. **Read Phase by Phase**:
   - Start with Phase 1 (Setup)
   - Read relevant blueprint sections
   - Implement that phase
   - Test before moving to next phase

2. **Reference During Coding**:
   - Check function specifications before writing functions
   - Verify data models when handling data
   - Review error handling for edge cases

3. **Follow the Order**:
   ```
   Phase 1: Setup → 01, 05, 12
   Phase 2: Config → 02, 03, 04
   Phase 3: Collection → 05, 06, 07, 08
   Phase 4: Preprocessing → 06, 07, 10
   Phase 5: Duplicates → 06, 07, 10
   Phase 6: Analysis → 04, 06, 07, 09, 10
   Phase 7: Storage → 04, 06, 07, 10
   Phase 8: Themes → 06, 07, 09, 10
   Phase 9: Digest → 06, 07, 09, 10
   Phase 10: Docs → 11, 12
   ```

---

## 🚀 Quick Start Guide

### Day 1 Morning: Setup & Collection (Phases 1-3)

**Read**:
- 01_Project_Overview.md
- 05_Module_Design.md
- 12_Deployment_Guide.md

**Implement**:
- Create folder structure
- Setup Git and virtual environment
- Install dependencies
- Create config files
- Implement collectors
- Test collection

**Verify**: `data/raw/articles.json` exists with articles

---

### Day 1 Afternoon: Processing (Phases 4-5)

**Read**:
- 03_Data_Models.md
- 07_Function_Specifications.md
- 10_Error_Handling.md

**Implement**:
- Preprocessing (cleaning, validation)
- Duplicate detection
- Test both phases

**Verify**: `data/processed/unique_articles.json` has clean, unique articles

---

### Day 1 Evening: AI Analysis (Phase 6)

**Read**:
- 04_API_Design.md
- 09_Prompt_Design.md
- 06_Class_Diagrams.md

**Implement**:
- Gemini client
- Article analyzer
- Test with a few articles
- Verify API key works

**Verify**: Gemini returns structured JSON

---

### Day 2 Morning: Storage & Themes (Phases 7-8)

**Read**:
- 04_API_Design.md (Google Sheets)
- 07_Function_Specifications.md
- 09_Prompt_Design.md (themes)

**Implement**:
- JSON storage
- Google Sheets integration (optional)
- Theme detector
- Statistics calculator
- Test full pipeline to this point

**Verify**: Articles in sheets, themes detected

---

### Day 2 Afternoon: Digest & UI & Documentation (Phases 9-11)

**Read**:
- 09_Prompt_Design.md (digest)
- 13_Web_UI_Design.md (Streamlit) ⭐
- 11_Test_Plan.md
- 12_Deployment_Guide.md

**Implement**:
- Markdown generator
- PDF generator
- **Streamlit UI (app.py)** ⭐
  - Dashboard page
  - Configuration page
  - Run pipeline page
  - Analytics page
  - View digest page
- Full integration test
- Create Builder's Note
- Update README
- Generate sample outputs
- Take UI screenshots

**Verify**: Professional PDF + interactive web UI generated 🚀

---

## 📊 Key Design Decisions

### 1. Agent Architecture
**Decision**: Use agent-based design with specialized agents for each phase

**Rationale**: 
- Modular and maintainable
- Easy to test individual components
- Clear responsibilities
- Professional structure

---

### 2. Gemini Only for AI
**Decision**: Use Gemini API exclusively, no OpenAI/Anthropic APIs

**Rationale**:
- Requirement specified by user
- Simplifies API management
- Single API key needed
- Cost-effective for demo

---

### 3. Dual Storage (JSON + Google Sheets)
**Decision**: Always save to JSON, optionally to Google Sheets

**Rationale**:
- JSON backup ensures data safety
- Google Sheets provides queryability
- Don't block pipeline if Sheets fails
- Easy to inspect and debug

---

### 4. Python Statistics + Gemini Insights
**Decision**: Calculate counts in Python, use Gemini for interpretation

**Rationale**:
- Python is fast and deterministic for counting
- Gemini is best for themes and insights
- Reduces token usage
- More reliable results
- Good engineering practice

---

### 5. Title-Based Duplicate Detection
**Decision**: Compare titles only, not full content

**Rationale**:
- Fast and simple
- Sufficient for demo
- Content comparison is complex and slow
- 90% similarity threshold works well

---

### 6. 4-Second Rate Limiting
**Decision**: Wait 4 seconds between Gemini API calls

**Rationale**:
- Free tier: 15 requests/minute
- 4 seconds = safe margin
- Prevents rate limit errors
- Acceptable for 20-30 articles

---

### 7. Progressive Enhancement
**Decision**: Core features first, optional features clearly marked

**Rationale**:
- JSON storage (required) before Google Sheets (optional)
- Basic collection before advanced scraping
- Manual testing before unit tests
- Meets deadline without over-engineering

---

## ⚠️ Critical Reminders

### Before Starting

1. ✅ Gemini API key obtained
2. ✅ All 10 phases understood
3. ✅ Blueprint documents reviewed
4. ✅ 2-day timeline planned
5. ✅ Development environment ready

### During Development

1. ✅ Follow blueprint specifications
2. ✅ Test each phase before moving forward
3. ✅ Log everything (use logger, not print)
4. ✅ Handle errors gracefully
5. ✅ Save progress frequently (Git commits)

### Before Submission

1. ✅ Full pipeline runs successfully
2. ✅ Sample outputs generated
3. ✅ README.md complete
4. ✅ Builder's Note created
5. ✅ No API keys in repository
6. ✅ All requirements met

---

## 📁 Expected Repository Structure

```
newsletter-research-agent/
├── README.md
├── requirements.txt
├── .gitignore
├── .env
├── main.py
├── IMPLEMENTATION_BLUEPRINT.md  ← This file
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── sources.py
│   ├── categories.py
│   └── prompts.py
│
├── src/
│   ├── __init__.py
│   ├── agents/
│   ├── collectors/
│   ├── preprocessing/
│   ├── duplicate/
│   ├── ai/
│   ├── storage/
│   └── utils/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
│
├── docs/
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
├── sample_output/
│   ├── sample_sheet.csv
│   ├── weekly_digest.pdf
│   └── weekly_digest.md
│
├── logs/
│   └── research_agent_YYYYMMDD.log
│
└── tests/
    ├── __init__.py
    ├── test_collector.py
    ├── test_preprocessing.py
    ├── test_ai.py
    └── test_storage.py
```

---

## 🎓 Learning Outcomes

By following this blueprint, you will demonstrate:

✅ **Software Architecture**: Agent-based design with clear separation of concerns
✅ **API Integration**: Gemini API for AI, Google Sheets for storage
✅ **Data Pipeline**: Multi-stage processing from raw to insights
✅ **Error Handling**: Graceful degradation and recovery
✅ **Documentation**: Professional technical documentation
✅ **Project Management**: Phased implementation within timeline
✅ **Best Practices**: Logging, configuration, modularity

---

## 🔗 Navigation

- **Start Here**: `docs/01_Project_Overview.md`
- **Architecture**: `docs/02_System_Architecture.md`
- **Implementation**: `docs/05_Module_Design.md` → `docs/06_Class_Diagrams.md` → `docs/07_Function_Specifications.md`
- **Setup & Run**: `docs/12_Deployment_Guide.md`
- **Testing**: `docs/11_Test_Plan.md`

---

## ✅ Blueprint Status

| Document | Status | Purpose |
|----------|--------|---------|
| 01_Project_Overview.md | ✅ Complete | What & Why |
| 02_System_Architecture.md | ✅ Complete | High-level design |
| 03_Data_Models.md | ✅ Complete | Data structures |
| 04_API_Design.md | ✅ Complete | External APIs |
| 05_Module_Design.md | ✅ Complete | File organization |
| 06_Class_Diagrams.md | ✅ Complete | OOP design |
| 07_Function_Specifications.md | ✅ Complete | Function details |
| 08_Data_Flow.md | ✅ Complete | Pipeline flow |
| 09_Prompt_Design.md | ✅ Complete | AI prompts |
| 10_Error_Handling.md | ✅ Complete | Error strategy |
| 11_Test_Plan.md | ✅ Complete | Testing approach |
| 12_Deployment_Guide.md | ✅ Complete | Setup & run |

---

## 🚀 Ready to Build

You now have a complete blueprint covering every aspect of the system:

- ✅ **What to build**: All features and requirements specified
- ✅ **How to build**: Architecture and design decisions documented
- ✅ **What to code**: Every class, function, and data structure defined
- ✅ **How to test**: Testing strategy and checklist provided
- ✅ **How to deploy**: Installation and configuration guide ready

**Next Step**: Begin Phase 1 implementation following `docs/12_Deployment_Guide.md`

---

**Blueprint Version**: 1.0
**Created**: 2026-07-05
**For**: AI Research Agent Internship Demo
**Timeline**: 2-day implementation
**Status**: Complete and ready for implementation 🔥⚔️


---

### ⭐ NEW: 13 - Web UI Design (Streamlit)
**Location**: `docs/13_Web_UI_Design.md`

**Contains**:
- Complete Streamlit UI design
- 5 pages: Home, Configuration, Run Pipeline, Analytics, View Digest
- Interactive charts and visualizations
- Live progress tracking
- Professional dashboard
- Mobile-responsive layout

**Purpose**: Make project visually impressive and easy to demo

**Why This is Critical**:
- ✅ Makes project 10x more impressive
- ✅ Easy live demo
- ✅ Shows full-stack capability
- ✅ Professional appearance
- ✅ User-friendly interface
- ✅ Can deploy to Streamlit Cloud (free!)

**Impact**: UI adds ~2-3 hours but provides 10x visual impact! 🔥

---

## 🎯 Updated Timeline with UI

### Day 2 Afternoon (5 hours) - REVISED
- ✅ Phase 9: Digest Generation (1.5 hours)
- ✅ **Phase 10: Web UI (Streamlit)** (2.5 hours) ⭐
- ✅ Phase 11: Documentation (1 hour)

**UI Features**:
- Interactive dashboard with metrics
- Live pipeline execution with progress bars
- Analytics with charts (plotly)
- Digest preview and download
- Configuration management

**Result**: Professional, demo-ready application! 🚀
