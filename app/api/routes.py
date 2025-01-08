from fastapi import APIRouter, HTTPException
from app.models.problem import Problem, ProblemAnalysis
from app.models.features.level1.analyzer import Level1Analyzer

router = APIRouter()
level1_analyzer = Level1Analyzer()

@router.post("/analyze/problem", response_model=ProblemAnalysis)
async def analyze_problem_route(problem: Problem):
    try:
        problem_dict = {
            'description': problem.description,
            'input': problem.input,
            'output': problem.output
        }
        
        analysis_result = await level1_analyzer.analyze(problem_dict)
        
        return ProblemAnalysis(
            problem_id=problem.problem_id,
            analysis=analysis_result,
            algorithm_type="Queue",
            approach="시뮬레이션",
            time_complexity="O(n)",
            space_complexity="O(n)"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
