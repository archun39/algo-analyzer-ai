from app.models.model import Model
from app.models.features.level1.prompt import LEVEL1_ANALYSIS_PROMPT
from typing import Dict
from app.models.problem import ProblemAnalysis
import asyncio
import json
import re

class Level1Analyzer(Model):
    def __init__(self):
        super().__init__()
        self.prompt = LEVEL1_ANALYSIS_PROMPT
    
    async def analyze(self, problem: Dict) -> ProblemAnalysis:
        try:
            prompt_value = self.prompt.format(
                problem_description=problem.get('description', ''),
                input_description=problem.get('input', ''),
                output_description=problem.get('output', ''),
                time_limit=problem.get('time_limit', ''),
                memory_limit=problem.get('memory_limit', ''),
                tags=', '.join(problem.get('tags', []))
            )
        

            analysis = await self.llm.ainvoke(prompt_value)
            print(analysis)
            result = await self.parse_analysis(analysis)
            
            return result
            
        except Exception as e:
            raise Exception(f"Level 1 분석 중 오류 발생: {str(e)}")

    async def parse_analysis(self, analysis: str) -> ProblemAnalysis:
        # analysis가 AIMessage 객체일 경우 .content 속성을 통해 문자열 추출
        if hasattr(analysis, 'content'):
            analysis = analysis.content
        
        # JSON 형식의 문자열만 추출 (중괄호 { } 포함 부분 찾기)
        json_match = re.search(r'\{.*\}', analysis, re.DOTALL)
        if not json_match:
            raise Exception("분석 결과에서 JSON 데이터를 찾을 수 없습니다.")
        
        json_str = json_match.group()
        
        # JSON 문자열 파싱
        analysis_data = json.loads(json_str)
        
        return ProblemAnalysis(
            problem_goal=analysis_data.get('1. 핵심 목표', ''),
            problem_approach=analysis_data.get('2. 접근 방식', ''),
            problem_condition=analysis_data.get('3. 문제 조건', ''),
            time_complexity=analysis_data.get('4. 시간 복잡도', ''),
            space_complexity=analysis_data.get('5. 공간 복잡도', ''),
            problem_type=analysis_data.get('6. 문제 유형 분석', ''),
            data_structure=analysis_data.get('7. 자료구조', ''),
            boundary_values=analysis_data.get('8. 경계값', ''),
            special_cases=analysis_data.get('9. 특수 케이스', ''),
            error_handling=analysis_data.get('10. 에러 처리', '')
        )
