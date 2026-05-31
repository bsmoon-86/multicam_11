# [실습 1] Docstring Generation
# 미션: AI에게 "Google Style Docstring과 Type Hint를 추가해줘"라고 요청하세요.
import math

def calculate_compound_interest(p, r, n, t):
    # p: principal, r: rate, n: compounds/year, t: years
    amount = p * (1 + r/n) ** (n*t)
    return amount

def sphere_volume(radius):
    if radius < 0: raise ValueError("Negative radius")
    return (4/3) * math.pi * (radius ** 3)
