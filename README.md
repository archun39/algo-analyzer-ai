# algo-analyzer-ai

알고리즘 문제 분석 AI 서버

## 프로젝트 소개

이 프로젝트는 알고리즘 문제에 대한 분석을 수행하는 AI 서버입니다. FastAPI와 LangChain, 그리고 OpenAI GPT 모델을 활용하여 알고리즘 문제를 분석하고, 문제의 시간 복잡도, 공간 복잡도, 알고리즘 유형, 사용된 자료구조, 구현 로직 등 다양한 분석 정보를 생성합니다. 서버는 RESTful API를 통해 외부 클라이언트와 연동되며, Docker를 통해 컨테이너화 되어 배포됩니다.

## 기능

- **문제 분석 요청 및 결과 처리**
  - 문제 정보를 기반으로 AI 분석 서버에 문제 분석 요청을 전달합니다.
  - GPT 기반 LLM과 LangChain을 활용하여 문제의 복잡도, 알고리즘 유형 등 상세 분석을 수행합니다.

- **LangChain 및 CoT(Chain-of-Thought) 활용**
  - LangChain을 이용하여 프롬프트 템플릿, LLM 호출, 출력 파서를 체인 형태로 구성하여 효율적인 분석을 수행합니다.
  - 프롬프트 내 단계별 사고(Chain-of-Thought) 유도를 통해 분석 과정과 근거를 상세히 제공합니다.

- **RESTful API 제공**
  - FastAPI 엔드포인트를 통해 외부 검색, 분석 요청 및 결과 반환을 지원합니다.

- **Docker 컨테이너화**
  - Docker 및 Docker Compose를 활용하여 서비스 배포 및 관리를 효율적으로 수행합니다.

## 기술 스택

- **프로그래밍 언어**: Python 3.x
- **웹 프레임워크**: FastAPI
- **LLM 연동 및 프롬프트 관리**: OpenAI GPT, LangChain
- **데이터 모델링**: Pydantic
- **컨테이너화**: Docker, Docker Compose
- **기타**: Uvicorn

## 환경 설정

### 환경 변수

- `OPENAI_API_KEY`: OpenAI API 키 (GPTModel에서 사용)
- `MODEL_NAME`: 사용 중인 모델 버전을 지정 (서버 실행 시 로그 출력)

`.env` 파일 또는 환경 변수 설정을 통해 위 변수들을 설정합니다.

### 실행 방법

1. **환경 변수 설정**
   - `.env` 파일 또는 환경 변수를 통해 `OPENAI_API_KEY`와 `MODEL_NAME` 등을 설정합니다.

2. **Docker Compose 사용**
   - 프로젝트 루트 디렉토리에서 다음 명령어로 Docker 컨테이너를 빌드 및 실행합니다:
     ```bash
     docker-compose up --build
     ```

3. **로컬 실행 (FastAPI 단독 실행)**
   - 다음 명령어로 FastAPI 서버를 로컬에서 실행할 수 있습니다:
     ```bash
     uvicorn app.main:app --reload
     ```

## 폴더 구조

```
algo-analyzer-ai/
├── app/
│   ├── api/              # FastAPI 엔드포인트 구성
│   │   ├── features/     # 단계별 분석 기능 (예: level1 등)
│   │   ├── base_llm.py
│   │   ├── gpt_model.py
│   │   ├── problem.py
│   │   └── model.py
│   └── main.py           # FastAPI 애플리케이션 진입점
├── Dockerfile            # 애플리케이션 도커 파일
├── docker-compose.yml    # Docker Compose 구성 파일
└── README.md             # 프로젝트 개요
```

## 추가 정보

- **로그 출력**: 서버 실행 시, `gpt_model.py`의 initialize 메서드에서 현재 사용 중인 모델 버전이 콘솔에 출력됩니다.
- **세부 분석**: LangChain 및 CoT 기반 프롬프트를 활용하여, 문제 분석 과정의 단계별 사고와 근거를 자세히 제공합니다.
- **확장성**: 향후 분석 모델 또는 단계(Level2 분석 등)의 추가를 염두에 두고 설계되었습니다.

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.