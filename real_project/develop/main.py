from mitmproxy import http
import json
from module import *
from filter import *

# mitmdump --ssl -s main.py --mode regular@8082

# 필터링할 키워드 목록
FILTER_URLS_FILE = 'filter/url.txt' 

FILTER_URLS = filterd_target_from_file(FILTER_URLS_FILE)

# request 
def request(flow: http.HTTPFlow) -> None:
    
    # URL FILTER
    if flow.request.pretty_url in FILTER_URLS:
        flow.response = response_make()
    
    # ChatGPT와 관련된 요청을 필터링하기 위해 URL 확인 (예시 URL, 실제로는 OpenAI의 API URL 사용)
    if "chatgpt.com" in flow.request.pretty_url:
        filter_gpt_prompt(flow)


