from pydantic import BaseModel
from typing import Optional

class Problem(BaseModel):
    problem_id: int
    title: str
    level: str
    tags: str
    average_tries: float
    description: str
    input: str
    output: str

class ProblemAnalysis(BaseModel):
    problem_id: int
    analysis: str
    algorithm_type: str
    approach: str
    time_complexity: str
    space_complexity: str
