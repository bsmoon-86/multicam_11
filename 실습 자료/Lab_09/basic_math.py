# [실습 1] 기본 단위 테스트 생성
# 상황: 아주 기초적인 함수지만 테스트 코드가 없습니다.
# 미션: AI에게 "AAA 패턴을 지켜서 Pytest 코드를 짜줘"라고 요청하세요.

def calculate_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be positive")
    return width * height

def is_even(number):
    return number % 2 == 0
