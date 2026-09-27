# 🤖 SentinelBot - Enterprise Python Automation Capstone Project

**Developer:** Sujal Bendkar | **ID:** `RAB-2026-9471669A59`  
**Track:** Python Software Engineering (RabTech Academy)  
**Task 06:** Enterprise Python Automation Capstone Project (GRAND FINALE)  

---

## 📌 Project Overview
`sentinelbot` is an end-to-end, production-grade Python automation capstone application. It integrates live backend API telemetry data fetching, statistical analytics processing, automated ReportLab PDF report generation, and automated cron/interval background scheduling with a clean CLI interface.

---

## 🏛️ System Architecture

```text
[ 🌐 Telemetry APIs (CoinGecko / Fallback Data) ]
                       │
                       ▼
[ 📡 TelemetryAPIClient (Requests + Retry Logic) ]
                       │
                       ▼
[ ⚙️ AnalyticsProcessor (Moving Averages + Sentiment Tags) ]
                       │
                       ▼
[ 📄 PDFReportEngine (ReportLab Multi-Page PDF Generator) ]
                       │
                       ▼
[ ⏰ AutomationScheduler (Cron / Interval Background Runner) ]
                       │
                       ▼
[ 🎓 SentinelBot_Executive_Report.pdf (Certification Deliverable) ]
```

---

## 🛠️ Features & Highlights

* **🤖 Backend API Integration:** Fetches live market & telemetry data via HTTP APIs (`requests`) with fallback datasets.
* **⚙️ Analytics Processor:** Calculates averages, top gainers/losers, risk indicators, and overall market sentiment.
* **📄 Automated PDF Report Engine:** Publication-grade ReportLab PDF generator with headers, summary metrics, formatted data tables, and color-coded styles.
* **⏰ Automated Scheduler:** Interval/cron background runner using `schedule` for automated report generation cycles.
* **📦 Packaged CLI Tool:** Package manifest with `pyproject.toml` and CLI entry points (`sentinelbot`).
* **🧪 Unit Testing Suite:** Automated unit tests covering API fallbacks, analytics engine, and PDF creation.

---

## 🚀 Quick Start & Usage

```bash
# 1. Install dependencies
pip install -r requirements.txt
pip install -e .

# 2. Run Instant Capstone PDF Report Generator
python run_capstone.py
# OR
sentinelbot

# 3. Run Automated Background Scheduler (Runs every 10 seconds)
sentinelbot --schedule 10

# 4. Run Automated Unit Tests
python -m unittest discover tests
```

---

## 📋 Repository Structure
```text
RabTech-Python-Task06-Enterprise-Capstone/
├── requirements.txt                   # Dependencies (reportlab, requests, schedule)
├── pyproject.toml                     # Package manifest
├── README.md                          # Comprehensive documentation & architecture diagram
├── run_capstone.py                    # One-click launcher script
├── sentinelbot/                       # Main Python package
│   ├── __init__.py                    # Version metadata
│   ├── api_client.py                  # Telemetry API client
│   ├── analytics.py                   # Statistical analytics engine
│   ├── pdf_generator.py               # ReportLab PDF report generator
│   ├── scheduler.py                   # Automated background scheduler
│   └── main.py                        # CLI entry point
└── tests/                             # Unit tests
    └── test_capstone.py               # Capstone unit tests
```

---

## 👤 Author & Certification Credits
* **Developer:** Sujal Bendkar
* **Batch:** `BATCH-SEP-2026`
* **Academy:** RabTech Academy - Python Software Engineering Internship
