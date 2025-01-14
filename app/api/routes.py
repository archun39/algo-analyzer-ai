from fastapi import APIRouter, HTTPException
from app.models.problem import Problem, ProblemAnalysis
from app.models.features.level1.analyzer import Level1Analyzer

router = APIRouter()
level1_analyzer = Level1Analyzer()

@router.post("/analyze/problem", response_model=ProblemAnalysis)
async def analyze_problem_route(problem: Problem) -> ProblemAnalysis:
    try:
        

        analysis_result = await level1_analyzer.analyze(problem)
        
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
