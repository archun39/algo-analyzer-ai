from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from app.models.problem import ProblemAnalysis

level1_analysis_template_json = """
시스템 메시지:
당신은 문제 해결 과정을 체계적으로 안내해 주는 튜터/도우미 역할을 맡았습니다. 
사용자는 특정 알고리즘 문제(또는 코드를) 제시했을 때, 다음 네 가지 단계별 로직에 따라 
명확하고 구체적인 설명을 듣고자 합니다.

[문제 정보]
문제 설명: {problem_description}
입력 조건: {input_description}
출력 조건: {output_description}
시간 제한 : {time_limit}
공간 제한 : {memory_limit}
알고리즘 유형 : {tags}

[단계별 로직]
1. 복잡도 구하기
- ({input_description}, {output_description}, {time_limit}, {memory_limit})을 통하여 대략적인 시간 복잡도와 공간 복잡도를 구한다.
- 대략적인 시간 복잡도와 공간복잡도를 {problem_description}에 따라 정확하게 구한다.
- 각각 Big-O 표기법으로 표현하고 근거있게 설명한다.

2. 문제 해결 방법 정리
- 위 알고리즘 유형 목록과 {tags}를 바탕으로 문제에 맞는 알고리즘 유형을 찾고, 선택 근거를 명확히 기술한다.

3. 자료구조
- 분석한 알고리즘 유형과 문제에 적합한 자료구조를 기술한다.

4. 문제 해결 방법 구현
- 알고리즘 유형, 자료구조, 문제 설명, 입력/출력 조건, 시간/공간 제한을 바탕으로 구현 로직을 단계적으로 설명한다.

위를 통해 알 수 있는 결과들을 반드시 아래 JSON 출력 형식을 지켜서 출력하세요:
// 예시 : 
```json
{{
  "time_complexity" : "",
  "time_complexity_reasoning" : "",
  "space_complexity" : "",
  "space_complexity_reasoning" : "",
  "algorithm_type" : "",
  "algorithm_type_reasoning" : "",
  "data_structures" : "",
  "data_structures_reasoning" : "",
  "solution_implementation" : "",
  "solution_implementation_reasoning" : ""
}}
"""

LEVEL1_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=[
        "problem_description",
        "input_description",
        "output_description",
        "time_limit",
        "memory_limit",
        "tags"
    ],
    template=level1_analysis_template_json,
)
