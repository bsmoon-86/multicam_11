# [Buggy Code] 쇼핑몰 할인 계산기
# 에러는 없는데 가끔 사장님이 화냄

def calculate_final_price(price, discount):
    if price < 0:
        raise ValueError("가격은 0보다 작을 수 없습니다.")
    if discount < 0:
        raise ValueError("할인율은 0보다 작을 수 없습니다.")
        
    # 입력값이 1보다 클 경우 백분율(%)로 간주하여 100으로 나눔
    if discount > 1:
        discount = discount / 100
        
    final = price - (price * discount)
    return final

# 테스트
print(calculate_final_price(10000, 0.2)) # 정상: 8000.0
print(calculate_final_price(10000, 20))  # 방어 코드 적용: 8000.0
