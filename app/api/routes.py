from fastapi import APIRouter, HTTPException
from app.models.problem import Problem, ProblemAnalysis
from app.services.llm_service import analyze_problem

router = APIRouter()

@router.post("/analyze", response_model=ProblemAnalysis)
async def analyze_problem_route(problem: Problem):
    try:
        result = await analyze_problem(problem)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
