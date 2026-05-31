# [실습 2] 난해한 정규식 해석
# 상황: 로그 파일에서 특정 패턴을 찾는 코드인데, 도저히 해석이 불가능합니다.
# 미션: AI에게 "이 정규식 패턴을 구성 요소별로 쪼개서 한글로 설명해줘"라고 요청하세요.

import re

log_line = '127.0.0.1 - - [10/Oct/2023:13:55:36 +0900] "GET /api/v1/user HTTP/1.1" 200 2326'

# 도대체 무엇을 추출하는 정규식일까요?
pattern = r'^(S+) S+ S+ [([w:/]+s[+-]d{4})] "(S+) (S+)s*(S+)?s*" (d{3}) (d+)'

match = re.match(pattern, log_line)
if match:
    print("Match found!")
