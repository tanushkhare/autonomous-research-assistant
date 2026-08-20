from fastapi import APIRouter, HTTPException
from backend.app.schemas.research_schema import ResearchTaskRequest, ResearchBriefResponse
from backend.app.services.research_service import research_agent

router = APIRouter(prefix="/api/v1/research", tags=["Autonomous Research Agent"])

@router.post("/execute", response_model=ResearchBriefResponse)
async def run_research_task(payload: ResearchTaskRequest):
    try:
        result = research_agent.execute_research_cycle(
            topic=payload.topic,
            depth=payload.depth_level,
            focus=payload.focus_areas
        )
        return ResearchBriefResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/task/{task_id}", response_model=ResearchBriefResponse)
async def get_task_result(task_id: str):
    if task_id not in research_agent.research_cache:
        raise HTTPException(status_code=404, detail="Research task ID not found.")
    return ResearchBriefResponse(**research_agent.research_cache[task_id])
