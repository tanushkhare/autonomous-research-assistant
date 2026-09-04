# ⚡ Autonomous AI Research Assistant

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://autonomous-research-assistant-web.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://autonomous-research-assistant-web.vercel.app](https://autonomous-research-assistant-web.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Multi-step autonomous agentic research planner that decomposes complex queries into multi-hop literature synthesis with real-time academic source validation (arXiv, Tavily) and verified DOI citations.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** Python, FastAPI, Tavily / ArXiv API, AsyncIO
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Zero Hallucinated Citations:** Hardcoded reference strings replaced with verified metadata DOI lookups.
* **Source Diversity Tracking:** Logs distinct domain counts and source origin types.
* **Configurable Search Depth:** Supports rapid summaries versus deep multi-hop synthesis.

---

## 🚀 API Contracts
```http
POST /api/v1/research/execute
Content-Type: application/json

Request Payload:
{
  "topic": "High-Throughput Vector Databases in Multi-Tenant Cloud Architectures",
  "depth": "deep"
}

Response (200 OK):
{
  "status": "COMPLETED",
  "sub_queries": [
    "Vector indexing memory bounds under HNSW",
    "Multi-tenant isolation techniques in pgvector and ChromaDB"
  ],
  "synthesis": "Decoupling vector indexing from background garbage collection preserves sub-20ms retrieval SLAs.",
  "citations": [
    {"source": "arXiv:2403.11982", "title": "Scalable Vector Search in Cloud Environments", "verified": true}
  ]
}

GET /health
Response: {"status": "healthy"}

💻 Local Quickstart

Bash
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v