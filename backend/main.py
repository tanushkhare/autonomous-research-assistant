from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import research_router
import uvicorn

app = FastAPI(
    title="Autonomous Research Assistant API",
    description="Multi-step agentic research planner, literature synthesizer, and technical brief generator.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(research_router.router)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "autonomous-research-assistant", "agent_loop": "Sequential Task Decomposition"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
