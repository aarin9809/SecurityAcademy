from mitmproxy import http
from mitmproxy import ctx
import json

def responseheaders(flow: http.HTTPFlow):
    # 응답 헤더에서 'Transfer-Encoding'이 'chunked'인 경우 처리
    if flow.response.headers.get("Transfer-Encoding") == "chunked":
        ctx.log.info(f"Chunked response from {flow.request.pretty_url}")

def response(flow: http.HTTPFlow):
    # SSE 혹은 chunked transfer로 스트리밍 응답이 올 때 응답 내용 확인
    if "text/event-stream" in flow.response.headers.get("Content-Type", ""):
        content = flow.response.content.decode("utf-8", errors="replace")
        events = content.splitlines()

        for event in events:
            if event.startswith("data:"):
                # 'data:'로 시작하는 스트리밍 데이터 출력
                data = event[5:].strip()
                ctx.log.info(f"Streamed data: {data}")
                try:
                    # 추출된 데이터를 JSON으로 파싱
                    json_data = json.loads(data)

                    # JSON 데이터에서 원하는 데이터를 추출
                    try:
                        if json_data['message']['id'] != None:
                            message_id = json_data['message']['id']
                            content_parts = json_data['message']['content']['parts']

                            # 원하는 대로 데이터를 수정하거나 사용할 수 있음
                            print(f"Message ID: {message_id}")
                            print(f"Content Parts: {content_parts}")

                            
                            # JSON 데이터를 수정 (예: message ID 변경)
                            json_data['message']['content']['parts'][0] = "해당 질문은 mitmproxy에 의해 필터링 처리 되었습니다!!"

                            content_parts = json_data['message']['content']['parts']
                            print(f"Content Parts: {content_parts}")

                            # 수정된 JSON 데이터를 다시 SSE 형식으로 변환
                            modified_event = f"data: {json.dumps(json_data)}"

                            # 수정된 이벤트를 원래 콘텐츠에 반영
                            content = content.replace(event, modified_event)

                            ctx.log.info(f"Modified content parts: {json_data['message']['content']['parts']}")
                            print("content ====== ", content)

                            flow.response.text = content
                        else:
                            print("message is null")
                    except:
                        print("message id is null")
                    
                except json.JSONDecodeError:
                    print("JSON 파싱 오류 발생")
            else:
                ctx.log.info(f"Other event: {event}")

    # 일반 HTTP 응답 출력 (필요 시)
    else:
        ctx.log.info(f"Response from {flow.request.pretty_url}: {flow.response.content[:100]}")  # 첫 100바이트만 출력
