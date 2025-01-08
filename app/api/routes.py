from fastapi import APIRouter, HTTPException
from app.models.problem import Problem, ProblemAnalysis
from app.models.features.level1.analyzer import Level1Analyzer

router = APIRouter()
level1_analyzer = Level1Analyzer()

@router.post("/analyze/problem", response_model=ProblemAnalysis)
async def analyze_problem_route(problem: Problem):
    try:
        problem_dict = {
            'problem_id': problem.problem_id,
            'description': problem.description,
            'input': problem.input,
            'output': problem.output,
            'time_limit': problem.time_limit,
            'memory_limit': problem.memory_limit,
            'tags': problem.tags
        }
        
        analysis_result = await level1_analyzer.analyze(problem_dict)
        
        return ProblemAnalysis(
            problem_goal=analysis_result.problem_goal,
            problem_approach=analysis_result.problem_approach,
            problem_condition=analysis_result.problem_condition,
            time_complexity=analysis_result.time_complexity,
            space_complexity=analysis_result.space_complexity,
            problem_type=analysis_result.problem_type,
            data_structure=analysis_result.data_structure,
            boundary_values=analysis_result.boundary_values,
            special_cases=analysis_result.special_cases,
            error_handling=analysis_result.error_handling
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
