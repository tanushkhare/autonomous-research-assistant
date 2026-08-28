from fastapi import APIRouter, HTTPException
from backend.app.schemas.research_schema import ResearchQueryRequest, ResearchReportResponse
from backend.app.services.research_service import research_agent

router = APIRouter(prefix="/api/v1/research", tags=["Autonomous Research Agent"])

@router.post("/query", response_model=ResearchReportResponse)
async def conduct_research(payload: ResearchQueryRequest):
    try:
        result = await research_agent.execute_research(payload.topic, payload.depth_level)
        return ResearchReportResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
