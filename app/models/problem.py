from pydantic import BaseModel, Field
from typing import List

# 요청 모델
class Problem(BaseModel):
    """문제 정보를 담는 모델"""
    problem_id: int
    description: str
    input: str
    output: str
    time_limit: str
    memory_limit: str
    tags: List[str]

# 응답 모델
class ProblemAnalysis(BaseModel):
    """문제 분석 결과를 담는 모델"""
    time_complexity: str = Field(..., description="시간 복잡도")
    time_complexity_reasoning: str = Field(..., description="시간 복잡도를 포함한 설명")
    space_complexity: str = Field(..., description="공간 복잡도")
    space_complexity_reasoning: str = Field(..., description="공간 복잡도를 포함한 설명")
    algorithm_type: str = Field(..., description="알고리즘 유형")
    algorithm_type_reasoning: str = Field(..., description="알고리즘 유형을 선택한 근거 설명")
    data_structures: str = Field(..., description="사용된 자료구조")
    data_structures_reasoning: str = Field(..., description="사용된 자료구조를 포함한 설명")
    solution_implementation: str = Field(..., description="문제 해결 방법의 구현 로직")
    solution_implementation_reasoning: str = Field(..., description="문제 해결 방법의 구현 로직을 포함한 설명")