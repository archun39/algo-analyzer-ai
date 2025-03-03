from langchain.prompts import PromptTemplate

level1_analysis_template_json = """
시스템 메시지:
당신은 문제 해결 과정을 체계적으로 안내해 주는 튜터/도우미 역할을 맡았습니다. 
사용자는 특정 알고리즘 문제(또는 코드를) 제시했을 때, 다음 네 가지 단계별 로직에 따라 
명확하고 구체적인 설명을 듣고자 합니다.

# 추가 요구사항:
- 최종 요약(핵심 정보)은 “timeCmplexity, spaceComplexity, algorithmType, dataStructures, solutionImplementation”
  부분에 작성하세요.
- 각 요약에 대한 근거(이유)는 “timeComplexityReasoning, spaceComplexityReasoning, algorithmTypeReasoning,
  dataStructuresReasoning, solutionImplementationReasoning” 부분에 작성하세요.
- 사용자는 “최종 요약”을 먼저 보고, 클릭 시 “세부 내용(근거)”를 볼 수 있다고 가정합니다.
  따라서 요약(=핵심)과 이유(=세부)를 구분해야 합니다.

[문제 정보]
문제 설명: {problemDescription}
입력 조건: {inputDescription}
출력 조건: {outputDescription}
시간 제한 : {timeLimit}
공간 제한 : {memoryLimit}
알고리즘 유형 : {tags}

[단계별 로직]
1. 복잡도 구하기
- 입력 조건, 출력 조건, 시간 제한, 공간 제한을 통하여 대략적인 시간 복잡도와 공간 복잡도를 구한다.
- 대략적인 시간 복잡도와 공간복잡도를 문제 설명에 따라 정확하게 구한다.
- 시간 복잡도는 시간 제한과 공간 제한을 통해 설명한다.
- 각각 Big-O 표기법으로 표현하고 근거있게 설명한다.

2. 문제 해결 방법 정리
--알고리즘 유형--
완전 탐색/백트래킹
그리디
정렬 & 이분 탐색
자료구조(스택, 큐, 세그먼트 트리, 펜윅 트리, 우선순위 큐, Union-Find 등)
동적 계획법(DP)
그래프(DFS/BFS, 최단 경로, MST, 플로우, 매칭 등)
문자열(KMP, 접미사 배열 등)
수학/정수론
기하 알고리즘
비트마스킹
시뮬레이션(구현)
기타 혼합 기법
- 위 알고리즘 유형 목록과 문제 설명을 바탕으로 문제에 맞는 알고리즘 유형을 찾고, 선택 근거를 명확히 기술한다.
- 이후 {tags}를 통해 검증한다.

3. 문제 해결 방법 구현
- 시간 복잡도와 공간 복잡도를 근거하여 문제 해결 방법을 생각한다.
- 알고리즘 유형, 자료구조, 문제 설명, 입력/출력 조건, 시간/공간 제한을 바탕으로 구현 로직을 번호를 만들어서 단계적으로 설명한다.


4. 자료구조
- 문제 해결 방법 구현에 사용된 자료구조들을 모두 기술한다.
- 중복되는 자료구조는 제거하고 기술한다.

위를 통해 알 수 있는 결과들을 반드시 아래 JSON 출력 형식을 지켜서 한국어로 번역하여 출력하세요:
// 예시 : 
```json
{{
  "problemId" : "{problemId}",
  "timeComplexity" : "",
  "timeComplexityReasoning" : "",
  "spaceComplexity" : "",
  "spaceComplexityReasoning" : "",
  "algorithmType" : "",
  "algorithmTypeReasoning" : "",
  "dataStructures" : "",
  "dataStructuresReasoning" : "",
  "solutionImplementation" : "",
  "solutionImplementationReasoning" : ""
}}

"""

LEVEL1_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=[
        "problemId",
        "problemDescription",
        "inputDescription",
        "outputDescription",
        "timeLimit",
        "memoryLimit",
        "tags"
    ],
    template=level1_analysis_template_json,
)
