from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class Model:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model_name = os.getenv("MODEL_NAME") 
        
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY가 설정되지 않았습니다.")
        
        if not self.model_name:
            raise ValueError("MODEL_NAME이 설정되지 않았습니다.")
            
        # Langchain ChatOpenAI 인스턴스 생성
        try:
            self.llm = ChatOpenAI(
                model_name=self.model_name,
                temperature=0.0,
                openai_api_key=self.api_key
            )
        except Exception as e:
            raise Exception(f"LLM 초기화 실패: {str(e)}")

    async def test_connection(self):
        """LLM 연결 테스트"""
        try:
            test_response = await self.llm.ainvoke("테스트 메시지입니다.")
            return True
        except Exception as e:
            print(f"LLM 연결 테스트 실패: {str(e)}")
            return False

    