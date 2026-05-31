# [Legacy Code] 작성자: 퇴사자A (2019)
# 건드리지 마시오. 돌아가긴 함.
import re

def is_valid_email(email):
    """이메일 주소의 유효성을 간략하게 검사합니다.

    문자열 내에 '@'가 포함되어 있고, '@'를 기준으로 두 부분으로 나뉘며,
    도메인 부분에 '.'이 포함되어 있는지 확인합니다.

    Args:
        email (str): 검사할 이메일 문자열.

    Returns:
        bool: 기본적인 이메일 형식을 만족하면 True, 그렇지 않으면 False.
    """
    if '@' in email:
        parts = email.split('@')
        if len(parts) == 2:
            if '.' in parts[1]:
                return True
    return False

def clean_phone_number(phone_number):
    """문자열(전화번호 등)에서 하이픈(-)과 공백을 제거합니다.

    Args:
        phone_number (str): 정제할 입력 문자열.

    Returns:
        str: 하이픈과 공백이 모두 제거된 문자열.
    """
    return phone_number.replace('-', '').replace(' ', '')
