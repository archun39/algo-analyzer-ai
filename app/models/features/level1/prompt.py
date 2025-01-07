from langchain_core.prompts import PromptTemplate

level1_analysis_template = """당신은 알고리즘 문제 분석 전문가입니다. 
주어진 문제의 설명, 입력 조건, 출력 조건을 바탕으로 상세한 분석을 제공해주세요.

[문제 설명]
{problem_description}

[입력 조건]
{input_description}

[출력 조건]
{output_description}

다음 형식에 맞춰 분석 결과를 제공해주세요:

1. 입력 조건:
- 입력 데이터의 형식과 제약조건을 상세히 설명

2. 출력 조건:
- 요구되는 출력 형식과 조건을 명확히 설명

3. 시간복잡도 분석:
- 예상되는 최적의 알고리즘 시간복잡도
- 시간복잡도 도출 근거

4. 공간복잡도 분석:
- 예상되는 공간복잡도
- 공간복잡도 도출 근거

5. 문제 이해:
- 문제의 핵심 목표
- 주요 제약사항
- 해결해야 할 핵심 과제

6. 문제 유형:
- 필요한 자료구조와 선택 이유
- 관련된 알고리즘 유형(태그)과 선정 근거

7. 입출력 제한사항 점검:
- 입력값의 범위와 제약조건 분석
- 출력 형식 관련 주의사항
- 예외 케이스 고려사항

<출력 예시>
1. 입력 조건:
- 입력 데이터의 형식과 제약조건을 상세히 설명

2. 출력 조건:
- 요구되는 출력 형식과 조건을 명확히 설명

3. 시간복잡도 분석:
- 예상되는 최적의 알고리즘 시간복잡도
- 시간복잡도 도출 근거

4. 공간복잡도 분석:
- 예상되는 공간복잡도
- 공간복잡도 도출 근거

5. 문제 이해:
- 문제의 핵심 목표
- 주요 제약사항
- 해결해야 할 핵심 과제

6. 문제 유형:
- 필요한 자료구조와 선택 이유
- 관련된 알고리즘 유형(태그)과 선정 근거

7. 입출력 제한사항 점검:
- 입력값의 범위와 제약조건 분석
- 출력 형식 관련 주의사항
- 예외 케이스 고려사항
"""

LEVEL1_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["problem_description", "input_description", "output_description"],
    template=level1_analysis_template
)
