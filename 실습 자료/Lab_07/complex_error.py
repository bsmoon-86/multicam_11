# [실습 2] Traceback Analysis
# 목표: 복잡한 에러 메시지를 AI에게 해석시킵니다.
# 미션: 에러 메시지 전체를 복사해서 AI에게 "원인을 쉽게 설명해줘"라고 하세요.

def process_data(data):
    return clean_data(data)

def clean_data(data):
    return analyze_data(data)

def analyze_data(data):
    # 여기서 에러 발생!
    return data['stats']['score'] + 10

user_input = {'name': 'Alice', 'stats': None}
process_data(user_input)
