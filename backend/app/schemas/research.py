from pydantic import BaseModel, Field
from typing import List

class ResearchRequest(BaseModel):
    topic: str = Field(..., description="The research topic or query to investigate")
    depth: str = Field("standard", description="Research depth: brief, standard, or deep")

class ResearchResponse(BaseModel):
    status: str
    topic: str
    summary: str
    key_findings: List[str]
    recommendation: str