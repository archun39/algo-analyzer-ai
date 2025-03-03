from app.models.model import Model
from app.models.features.level2.prompt import LEVEL2_ANALYSIS_PROMPT
from app.models.problem import ProblemAnalysis, Problem
from typing import Dict
from langchain.output_parsers import PydanticOutputParser

# LangChain import
from langchain.output_parsers import PydanticOutputParser

class Level2Analyzer(Model):
    def __init__(self):
        super().__init__()
        self.prompt = LEVEL2_ANALYSIS_PROMPT
        self.parser = PydanticOutputParser(pydantic_object=ProblemAnalysis)

    async def analyze(self, problem: Problem) -> ProblemAnalysis:
        try:
            #체인 생성
            analysis_chain = self.prompt | self.llm | self.parser

            # 입력 데이터 생성
            analysis_input = {
                "problemId": problem.problemId,
                "problemDescription": problem.description,
                "inputDescription": problem.input,
                "outputDescription": problem.output,
                "timeLimit": problem.timeLimit,
                "memoryLimit": problem.memoryLimit,
                "tags": ', '.join(problem.tags)
            }    

            # PromptTemplate에 필요한 변수를 키워드 인자로 넘김
            analysis_result = await analysis_chain.ainvoke(analysis_input)

            return analysis_result

        except Exception as e:
            raise Exception(f"Level 2 분석 중 오류 발생: {str(e)}")
