from mitmproxy import http
import json

# 필터링할 키워드 목록
FILTER_KEYWORDS = ["test", "test1", "test2"]
FILTER_URLS = ["naver.com", "daum.net"]

def request(flow: http.HTTPFlow) -> None:
    
    # URL FILTER
    print("URL========", flow.request.pretty_url)
    if flow.request.pretty_url == "https://www.naver.com/":
        print("CHECK URL")
        flow.response = http.Response.make(
            404,
            b"Filtered Page",
            {"Content-Type": "text/html"}            
        )
        print("response make=======")        
    
    # ChatGPT와 관련된 요청을 필터링하기 위해 URL 확인 (예시 URL, 실제로는 OpenAI의 API URL 사용)
    if "chatgpt.com" in flow.request.pretty_url:
        # 요청 본문 확인 (프롬프트 데이터가 들어있는 JSON)
        if flow.request.headers.get("Content-Type") == "application/json":
            try:
                data = flow.request.json()
                print("json_data = ", data)
                # 프롬프트 필드에 특정 키워드가 포함되어 있는지 확인
                                
                content = find_value(data, "parts")
                print("content===========", content)
                if any(keyword in content for keyword in FILTER_KEYWORDS):
                    print("matching=========")                    
                    # 프롬프트를 필터링할 경우, 사용자에게 경고 메시지 반환
                    flow.response = http.Response.make(
                        404,  # HTTP 상태 코드: 403 Forbidden
                        json.dumps({"error": "차단된 프롬프트입니다. 요청이 거부되었습니다."}),
                        {"Content-Type": "application/json"}
                    )
                    print("response make =========")                    
            except Exception as e:
                print(f"Error processing request: {e}")


def find_value(json_data, target_key):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == target_key:
                return value
            if isinstance(value, (dict, list)):
                result = find_value(value, target_key)
                if result is not None:
                    return result
    elif isinstance(json_data, list):
        for item in json_data:
            result = find_value(item, target_key)
            if result is not None:
                return result
    return None

