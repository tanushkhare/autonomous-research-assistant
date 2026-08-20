import streamlit as st
import requests
import json

st.set_page_config(page_title="Autonomous AI Research Assistant", layout="wide")

st.title("🤖 Autonomous AI Research & Technical Intelligence Agent")
st.markdown("Automated multi-step agentic decomposition, literature synthesis, and strategic briefing engine.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Research Commissioning")
    topic_input = st.text_input("Investigation Thesis / Topic", value="High-Throughput Vector Databases in Multi-Tenant Clouds")
    depth = st.selectbox("Investigation Depth", ["Technical", "Executive", "Comprehensive"])
    
    if st.button("Dispatch Autonomous Research Agent", type="primary"):
        with st.spinner("Decomposing subqueries, harvesting citations, and synthesizing findings..."):
            payload = {"topic": topic_input, "depth_level": depth, "focus_areas": ["Scalability", "Security"]}
            try:
                res = requests.post("http://localhost:8000/api/v1/research/execute", json=payload, timeout=10)
                if res.status_code == 200:
                    st.session_state["p02_result"] = res.json()
                    st.success("Research Dossier Generated!")
                else:
                    st.error(f"API Error: {res.text}")
            except Exception:
                st.warning("Backend API offline. Executing client-side agent synthesis simulation.")
                st.session_state["p02_result"] = {
                    "task_id": "sim_8401",
                    "topic": topic_input,
                    "executive_summary": f"Executive Synthesis for '{topic_input}': Production viability mandates decoupling indexing workers from API endpoints to guarantee sub-15ms p95 query SLAs.",
                    "detailed_findings": [
                        {
                            "subtopic": "Architecture & Ingestion Scale",
                            "summary": "Benchmarking confirms that partitioned HNSW vector graphs preserve search precision while halving index recreation overhead.",
                            "key_takeaways": ["40% memory saving via product quantization.", "Decoupled background indexing prevents latency spikes."],
                            "citations": ["IEEE Big Data (2025)", "ACM Distributed Computing"]
                        }
                    ],
                    "strategic_recommendations": [
                        "Enforce connection pooling and read replicas for vector metadata storage.",
                        "Isolate user tenant namespaces via cryptographically signed partition keys."
                    ]
                }

with col2:
    if "p02_result" in st.session_state:
        res = st.session_state["p02_result"]
        st.subheader(f"Dossier: {res['topic']}")
        
        st.markdown("### 📋 Executive Summary")
        st.info(res["executive_summary"])
        
        st.markdown("### 🔬 Detailed Findings & Citations")
        for finding in res["detailed_findings"]:
            with st.expander(f"📌 {finding['subtopic']}", expanded=True):
                st.write(finding["summary"])
                st.markdown("**Key Takeaways:**")
                for item in finding["key_takeaways"]:
                    st.write(f"- {item}")
                st.markdown("**Citations:**")
                st.caption(", ".join(finding["citations"]))
        
        st.markdown("### 🎯 Strategic Recommendations")
        for rec in res["strategic_recommendations"]:
            st.success(f"💡 {rec}")
