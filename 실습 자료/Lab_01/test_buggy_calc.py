import pytest
from buggy_calc import calculate_final_price

def test_calculate_final_price_normal():
    """정상적인 소수점 할인율 입력 (20%)"""
    assert calculate_final_price(10000, 0.2) == 8000

def test_calculate_final_price_integer_discount():
    """1보다 큰 정수 형태의 할인율 입력 방어 확인 (20)"""
    assert calculate_final_price(10000, 20) == 8000

def test_calculate_final_price_negative_price():
    """가격이 음수인 경우 예외 발생 검증"""
    with pytest.raises(ValueError, match="가격은 0보다 작을 수 없습니다."):
        calculate_final_price(-10000, 0.2)

def test_calculate_final_price_negative_discount():
    """할인율이 음수인 경우 예외 발생 검증"""
    with pytest.raises(ValueError, match="할인율은 0보다 작을 수 없습니다."):
        calculate_final_price(10000, -0.2)