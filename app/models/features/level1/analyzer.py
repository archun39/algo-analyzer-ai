from app.models.model import Model
from app.models.features.level1.prompt import LEVEL1_ANALYSIS_PROMPT
from app.models.problem import ProblemAnalysis, Problem
from typing import Dict
from langchain.output_parsers import PydanticOutputParser

class Level1Analyzer(Model):
    def __init__(self):
        super().__init__()
        self.prompt = LEVEL1_ANALYSIS_PROMPT
        self.parser = PydanticOutputParser(pydantic_object=ProblemAnalysis)

    async def analyze(self, problem: Problem) -> ProblemAnalysis:
        try:
            print("체인 생성 시작")

            analysis_chain = self.prompt | self.llm | self.parser
            print("체인 생성 완료")

            analysis_input = {
                "problem_description": problem.description,
                "input_description": problem.input,
                "output_description": problem.output,
                "time_limit": problem.time_limit,
                "memory_limit": problem.memory_limit,
                "tags": ', '.join(problem.tags)
            }    
            print(analysis_input)  
            # PromptTemplate에 필요한 변수를 키워드 인자로 넘김
            analysis_result = await analysis_chain.ainvoke(analysis_input)

            print("체인 실행 완료")
            return analysis_result

        except Exception as e:
            raise Exception(f"Level 1 분석 중 오류 발생: {str(e)}")
