from dotenv import load_dotenv
import openai
import os
from .base_llm import BaseLLM

class GPTModel(BaseLLM):
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        load_dotenv()
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model_name = os.getenv("MODEL_NAME")
        print(f"Using model version: {os.getenv('MODEL_NAME')}")
    
    async def generate_response(self, prompt: str, **kwargs):
        try:
            response = await self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"GPT 응답 생성 실패: {str(e)}") 