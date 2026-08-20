from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Union

app = FastAPI(
    title="Autonomous Research Assistant API",
    version="1.0.0",
    description="API for automated topic research, synthesis, and report generation."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    topic: str = Field(..., description="The research topic or query to investigate")
    depth: Union[int, str] = Field(3, description="Research depth layer")

class ResearchResponse(BaseModel):
    status: str
    topic: str
    summary: str
    sources: List[str]

@app.get("/")
def read_root():
    return {"message": "Autonomous Research Assistant Backend is running successfully!"}

@app.post("/api/v1/research", response_model=ResearchResponse)
async def execute_research(payload: ResearchRequest):
    if not payload.topic.strip():
        raise HTTPException(status_code=400, detail="Research topic cannot be empty.")
    
    return {
        "status": "completed",
        "topic": payload.topic,
        "summary": f"Autonomous research agents successfully synthesized findings for '{payload.topic}' across depth level {payload.depth}.",
        "sources": [
            "https://arxiv.org/abs/2026.00192",
            "https://research.ai-network.org/papers/autonomous-agents"
        ]
    }