from app.models.problem import Problem, ProblemAnalysis

async def analyze_problem(problem: Problem) -> ProblemAnalysis:
    # TODO: 실제 LLM 분석 로직 구현
    return ProblemAnalysis(
        problem_id=problem.problem_id,
        analysis="임시 분석 결과",
        algorithm_type="구현해야 할 알고리즘 유형",
        approach="문제 해결 접근 방법",
        time_complexity="O(n)",
        space_complexity="O(1)"
    )
