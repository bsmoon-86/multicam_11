# [실습 4] Legacy Code Testing
# 상황: 누군가 짜고 도망간 지저분한 코드입니다. 수정하기 전에 테스트부터 확보해야 합니다.
# 미션: AI에게 "이 코드의 기능을 검증하는 테스트를 먼저 짜고, 그 뒤에 코드를 깔끔하게 리팩토링해줘"라고 하세요.

def parse_user_data(data_str):
    # data_str 예시: "Hong,25,Seoul"
    parts = data_str.split(",")
    name = parts[0]
    age = int(parts[1])
    city = parts[2]
    
    # 나이가 0보다 작으면 에러? 그런 처리 없음.
    # 데이터가 부족하면? 인덱스 에러 남.
    return {"n": name, "a": age, "c": city}
