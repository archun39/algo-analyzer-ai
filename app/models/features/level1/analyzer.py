from app.models.model import Model
from app.models.features.level1.prompt import LEVEL1_ANALYSIS_PROMPT
from app.models.problem import ProblemAnalysis, Problem
from typing import Dict
from langchain.output_parsers import PydanticOutputParser
from langchain.chains import LLMChain

class Level1Analyzer(Model):
    def __init__(self):
        super().__init__()
        self.prompt = LEVEL1_ANALYSIS_PROMPT
        self.parser = PydanticOutputParser(pydantic_object=ProblemAnalysis)

    async def analyze(self, problem: Problem) -> ProblemAnalysis:
        try:
            #체인 생성
            analysis_chain = self.prompt | self.llm | self.parser

            # 입력 데이터 생성
            analysis_input = {
                "problem_description": problem.description,
                "input_description": problem.input,
                "output_description": problem.output,
                "time_limit": problem.time_limit,
                "memory_limit": problem.memory_limit,
                "tags": ', '.join(problem.tags)
            }    

            # PromptTemplate에 필요한 변수를 키워드 인자로 넘김
            analysis_result = await analysis_chain.ainvoke(analysis_input)

            return analysis_result

        except Exception as e:
            raise Exception(f"Level 1 분석 중 오류 발생: {str(e)}")
