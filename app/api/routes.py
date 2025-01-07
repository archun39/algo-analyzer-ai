from fastapi import APIRouter, HTTPException
from app.models.problem import Problem, ProblemAnalysis
from app.models.features.level1.analyzer import Level1Analyzer

router = APIRouter()
level1_analyzer = Level1Analyzer()

@router.post("/analyze", response_model=ProblemAnalysis)
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
            algorithm_type="분석 결과에서 추출",
            approach="분석 결과에서 추출",
            time_complexity="분석 결과에서 추출",
            space_complexity="분석 결과에서 추출"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
