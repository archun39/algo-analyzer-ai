from langchain import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# gpt-4o-mini

class Model:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model_name = os.getenv("MODEL_NAME") 
        
        # Langchain ChatOpenAI 인스턴스 생성
        self.llm = ChatOpenAI(
            model_name=self.model_name,
            temperature=0.0,
            openai_api_key=self.api_key
        )


    