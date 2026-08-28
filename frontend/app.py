import streamlit as st
import requests

st.set_page_config(page_title="Autonomous Research Assistant", layout="wide")

st.title("🔬 Autonomous Literature & Research Assistant")
st.markdown("Agentic search execution, verified technical source citation, and automated executive summarization.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Research Topic Ingest")
    topic = st.text_input("Technical Topic / Question", value="Distributed Consensus Raft")
    depth = st.selectbox("Synthesis Mode", ["deep", "fast"])

    if st.button("Execute Autonomous Research Agent", type="primary"):
        with st.spinner("Executing agentic search loop and verifying citations..."):
            try:
                res = requests.post("http://localhost:8000/api/v1/research/query", json={"topic": topic, "depth_level": depth}, timeout=10)
                if res.status_code == 200:
                    st.session_state["p02_result"] = res.json()
                    st.success("Research Report Synthesized!")
                else:
                    st.error(f"Agent Error: {res.text}")
            except Exception:
                st.warning("Backend offline. Running simulated literature aggregation.")
                st.session_state["p02_result"] = {
                    "research_id": "RES-SIM88",
                    "topic": topic,
                    "executive_summary": f"Synthesized analysis on '{topic}' citing canonical literature.",
                    "key_findings": [
                        "Deconstructs consensus into leader election, log replication, and safety.",
                        "Sub-50ms heartbeat intervals maintain high availability."
                    ],
                    "citations": [
                        {"title": "Raft: In Search of an Understandable Consensus Algorithm", "domain": "usenix.org", "summary": "Foundational consensus protocol.", "relevance_score": 0.98}
                    ],
                    "latency_ms": 42.5,
                    "timestamp": "2026-08-28T07:45:00Z"
                }

with col2:
    if "p02_result" in st.session_state:
        res = st.session_state["p02_result"]
        st.subheader(f"Report: {res['research_id']}")
        st.info(f"⏱️ Agent Latency: {res['latency_ms']} ms")
        
        st.markdown("#### Executive Summary")
        st.write(res["executive_summary"])
        
        st.markdown("#### Key Technical Findings")
        for finding in res["key_findings"]:
            st.markdown(f"• {finding}")
            
        st.markdown("#### Ground-Truth Citations")
        for cit in res["citations"]:
            with st.expander(f"📚 {cit['title']} ({cit['source_domain']})"):
                st.write(cit["summary"])
                st.caption(f"Relevance Score: {cit['relevance_score']}")
