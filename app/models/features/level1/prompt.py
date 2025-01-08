from langchain_core.prompts import PromptTemplate

level1_analysis_template = """당신은 알고리즘 문제 분석 전문가입니다. 
주어진 문제를 분석하여 최적의 해결 방법을 제시해야 합니다.

[문제 정보]
문제 설명: {problem_description}
입력 조건: {input_description}
출력 조건: {output_description}
시간 제한 : {time_limit}
공간 제한 : {memory_limit}
알고리즘 유형 : {tags}

다음 단계에 따라 문제를 체계적으로 분석해주세요:

1. 문제 이해:
- 핵심 목표: [문제가 요구하는 핵심 작업을 한 문장으로]

2. 문제 조건:
- 접근 방식: [문제 해결을 위한 단계별 접근 방법]
- 문제 조건: [문제에서 해결해야 하는 조건] ex) 알고리즘 순서, 알고리즘 동작 방식, 알고리즘 예외, 알고리즘 적으로 고려해야할 사항

3. 복잡도 분석: 
- 시간 복잡도: [{time_limit} 초 내에 해결 가능하고 {input_description} 입력 조건을 고려하여 Big-O 표기법으로 표현]
- 공간 복잡도: [{memory_limit} 메모리 내에 해결 가능하고 {input_description} 입력 조건을 고려하여 Big-O 표기법으로 표현]

4. 문제 유형 분석:
- 문제 유형 분석 근거: [{problem_description}에서 찾을 수 있는 {tags} 분석 근거]

5. 자료구조:
- 자료구조 분석 근거: [{problem_description}와 문제 유형 분석을 통해 알 수 있는 자료구조와 분석 근거]

6. 예외 케이스:
- 경계값: [최소/최대 입력값 처리]
- 특수 케이스: [{problem_description}에서 찾을 수 있는 특별한 상황]
- 에러 처리: [{problem_description}에서 찾을 수 있는 발생 가능한 예외 상황]

분석 이후 다음 출력 형식에 맞춰 JSON 형식으로 출력해주세요:

[출력 형식] 

1. 핵심 목표: [문제가 요구하는 핵심 작업을 한 문장으로]

2. 접근 방식: [문제 해결을 위한 단계별 접근 방법]

3. 문제 조건: [문제에서 해결해야 하는 조건] ex) 알고리즘 순서, 알고리즘 동작 방식, 알고리즘 예외, 알고리즘 적으로 고려해야할 사항을 번호 리스트를 통해 작성해줘

4. 시간 복잡도: [{time_limit} 초 내에 해결 가능하고 {input_description} 입력 조건을 고려하여 Big-O 표기법으로 표현]
     
5. 공간 복잡도: [{memory_limit} 메모리 내에 해결 가능하고 {input_description} 입력 조건을 고려하여 Big-O 표기법으로 표현]

6. 문제 유형 분석: [{problem_description}에서 찾을 수 있는 {tags} 분석 근거]

7. 자료구조: [{problem_description}와 문제 유형 분석을 통해 알 수 있는 자료구조와 분석 근거]

8. 경계값: [최소/최대 입력값 처리]

9. 특수 케이스: [{problem_description}에서 찾을 수 있는 특별한 상황]

10. 에러 처리: [{problem_description}에서 찾을 수 있는 발생 가능한 예외 상황]

분석 결과를 위 형식에 맞춰 상세히 설명해주세요.
각 항목에 대해 구체적인 근거와 함께 설명하되, 실제 구현 가능한 수준의 상세한 정보를 제공해주세요.
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
    template=level1_analysis_template
)
