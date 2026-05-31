# [실습 1] 비즈니스 로직 해독
# 상황: 변수명이 엉망이고 주석이 없는 쇼핑몰 가격 계산 코드입니다.
# 미션: AI에게 "이 코드가 수행하는 '할인 정책'을 비즈니스 용어로 요약해줘"라고 요청하세요.

def calculate_final_price(price: int, category_type: int, membership: str) -> int:
    """상품 카테고리와 멤버십 등급에 따른 할인이 적용된 최종 금액을 계산합니다."""
    final_price = float(price)
    
    # 1. 카테고리별 할인 적용
    if category_type == 1: # 가전(Electronics)
        if final_price > 100000:
            final_price *= 0.9   # 10% 할인
            
    elif category_type == 2: # 의류(Clothing)
        if membership == 'VIP':
            final_price *= 0.8   # 20% 할인
        else:
            final_price *= 0.95  # 5% 할인
    
    # 2. Season Off 게스트 혜택 추가 적용
    if membership == 'GUEST' and final_price > 50000:
        final_price -= 2000      # 2천원 정액 할인
    
    return int(final_price)
