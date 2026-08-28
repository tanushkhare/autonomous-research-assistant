from pydantic import BaseModel, Field
from typing import List, Optional

class ResearchQueryRequest(BaseModel):
    topic: str = Field(..., min_length=3, description="Research query or technical topic")
    depth_level: Optional[str] = Field(default="deep", description="Synthesis depth")

class AcademicCitation(BaseModel):
    title: str
    source_domain: str
    summary: str
    relevance_score: float

class ResearchReportResponse(BaseModel):
    research_id: str
    topic: str
    executive_summary: str
    key_findings: List[str]
    citations: List[AcademicCitation]
    latency_ms: float
    timestamp: str
