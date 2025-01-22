from pydantic import BaseModel, Field
from typing import List

# 요청 모델
class Problem(BaseModel):
    """문제 정보를 담는 모델"""
    problemId: int
    description: str
    input: str
    output: str
    timeLimit: str
    memoryLimit: str
    tags: List[str]

# 응답 모델
class ProblemAnalysis(BaseModel):
    """문제 분석 결과를 담는 모델"""
    problemId: int
    timeCmplexity: str = Field(..., description="시간 복잡도")
    timeComplexityReasoning: str = Field(..., description="시간 복잡도를 분석한 근거 설명")
    spaceComplexity: str = Field(..., description="공간 복잡도")
    spaceComplexityReasoning: str = Field(..., description="공간 복잡도를 분석한 근거 설명")
    algorithmType: str = Field(..., description="알고리즘 유형")
    algorithmTypeReasoning: str = Field(..., description="알고리즘 유형을 선택한 근거 설명")
    dataStructures: str = Field(..., description="사용된 자료구조")
    dataStructuresReasoning: str = Field(..., description="사용된 자료구조를 포함한 설명")
    solutionImplementation: str = Field(..., description="문제 해결 방법의 구현 로직")
    solutionImplementationReasoning: str = Field(..., description="문제 해결 방법의 구현 로직을 포함한 설명")
