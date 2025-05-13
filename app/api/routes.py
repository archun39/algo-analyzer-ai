from fastapi import APIRouter, HTTPException
from app.models.problem import Problem, ProblemAnalysis
from app.models.features.level1.analyzer import Level1Analyzer
from app.models.features.level2.analyzer import Level2Analyzer
import os
router = APIRouter()


@router.get("/health")
async def health_check():
    """GPT (OpenAI) 연결 상태 확인 엔드포인트"""

    analyzer = Level1Analyzer()
    
    ok = await analyzer.test_connection()
    return {"gpt_connected": ok}

level_setting = 1

@router.post("/internal/problems/{problemId}/analysis", response_model=ProblemAnalysis)
async def analyze_problem_route(problem: Problem) -> ProblemAnalysis:
    try:

        analyzer = set_level(level_setting)
        
        print(f"Using level: {level_setting}")

        analysis_result = await analyzer.analyze(problem)

        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def set_level(level: int):
    global level_setting
    level_setting = level
    
    if level_setting == 1:
        analyzer = Level1Analyzer()
    elif level_setting == 2:
        analyzer = Level2Analyzer()

    return analyzer