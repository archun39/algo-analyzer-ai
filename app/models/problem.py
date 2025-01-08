from pydantic import BaseModel
from typing import Optional, List

# 요청 모델
class Problem(BaseModel):
    problem_id: int
    description: str
    input: str
    output: str
    time_limit: str
    memory_limit: str
    tags: list[str]

# 응답 모델
class ProblemAnalysis(BaseModel):
    problem_goal: str
    problem_approach: list[str]
    problem_condition: list[str]
    time_complexity: str
    space_complexity: str
    problem_type: str
    data_structure: str
    boundary_values: str
    special_cases: str
    error_handling: str
