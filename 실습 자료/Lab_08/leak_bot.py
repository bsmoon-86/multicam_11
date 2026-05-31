# [실습 3] Hardcoded Secrets
# 미션: "코드 내 민감 정보를 찾고, python-dotenv를 사용하도록 리팩토링해줘."
def connect_aws():
    # ⚠️ 위험! 키 노출
    access_key = "AKIA_FAKE_KEY_12345"
    secret_key = "SECRET_FAKE_KEY_67890"
    print(f"Connecting with {access_key}...")
