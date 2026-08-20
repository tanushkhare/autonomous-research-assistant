from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class ResearchTaskRequest(BaseModel):
    topic: str = Field(..., min_length=5, description="Core topic or technical thesis to investigate")
    depth_level: Optional[str] = Field(default="Comprehensive", description="Research depth (Executive, Technical, Comprehensive)")
    focus_areas: Optional[List[str]] = Field(default_factory=list, description="Targeted focus areas or sub-domains")

class ResearchFinding(BaseModel):
    subtopic: str
    summary: str
    key_takeaways: List[str]
    citations: List[str]

class ResearchBriefResponse(BaseModel):
    task_id: str
    topic: str
    generated_at: datetime
    executive_summary: str
    detailed_findings: List[ResearchFinding]
    strategic_recommendations: List[str]
