# [실습 4] Security Audit
# 미션: "너는 보안 전문가야. 이 코드의 취약점을 분석하고 개선안을 리포트로 써줘."
import hashlib
import random

def register(user, pw):
    # 취약점: MD5 사용, 난수 예측 가능, 비밀번호 길이 미검사
    pw_hash = hashlib.md5(pw.encode()).hexdigest()
    token = random.randint(1000, 9999)
    print(f"User {user} registered. Hash: {pw_hash}")
