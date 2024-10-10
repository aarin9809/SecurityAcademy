from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    
    # 특정 URL 리다이렉션 
    print("URL========", flow.request.pretty_host)
    print("Request ======", flow.request)
    if flow.request.pretty_host == "www.jirandata.co.kr":
        flow.request.host = "mitmproxy.org"

    # 특정 URL 차단 페이지 응답
    if flow.request.pretty_url == "https://www.naver.com/":
        flow.response = http.Response.make(
            404,
            b"Filtered Page",
            {"Content-Type": "text/html"}
        )

def response(flow: http.HTTPFlow) -> None:
    
    if flow.response:
        # Convert bytes to string if necessary
        body_data = flow.response.content.decode('utf-8', errors='replace')        
        print(f"URL: {flow.request.url}")
        print(f"Response Body:\n{body_data}\n")

        modified_body = body_data.replace("양진모", "홍길동")

        flow.response.text = modified_body