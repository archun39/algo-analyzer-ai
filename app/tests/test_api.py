import requests
import json

def test_analyze_endpoint():
    url = "http://localhost:5000/api/analyze/problem"
    
    data = {
        "problem_id": 2164,
        "description": "N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다...",
        "input": "첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.",
        "output": "첫째 줄에 남게 되는 카드의 번호를 출력한다."
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        
        print("\n=== API 테스트 결과 ===")
        print(f"상태 코드: {response.status_code}")
        print(f"응답 내용: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        print("=====================\n")
        
    except requests.exceptions.ConnectionError:
        print("서버 연결 실패. 서버가 실행 중인지 확인하세요.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 에러 발생: {e}")
        print(f"에러 응답: {e.response.text}")
    except Exception as e:
        print(f"예상치 못한 에러 발생: {str(e)}")

if __name__ == "__main__":
    test_analyze_endpoint() 