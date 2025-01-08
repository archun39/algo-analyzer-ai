import asyncio
from app.models.model import Model

async def test_model():
    try:
        model = Model()
        print("Model 인스턴스 생성 성공")
        
        connection_test = await model.test_connection()
        if connection_test:
            print("LLM 연결 테스트 성공")
        else:
            print("LLM 연결 테스트 실패")
            
    except Exception as e:
        print(f"테스트 실패: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_model()) 