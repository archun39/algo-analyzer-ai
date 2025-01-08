from pydantic import BaseModel
from typing import Optional

# 요청 모델
class Problem(BaseModel):
    problem_id: int
    description: str
    input: str
    output: str

# 응답 모델
class ProblemAnalysis(BaseModel):
    problem_id: int
    analysis: str              # GPT의 상세 분석 결과
    algorithm_type: str        # 예: "Queue", "Stack", "Graph" 등
    approach: str             # 문제 해결 접근 방식
    time_complexity: str      # 예: "O(n)", "O(n log n)" 등
    space_complexity: str     # 예: "O(n)", "O(1)" 등
