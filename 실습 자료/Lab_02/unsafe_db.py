import os
# [실습 1] DB 보안
# 아래 코드는 데이터베이스 접속 정보를 하드코딩하고 있습니다.
# 만약 이 파일이 유출되면 해커가 DB를 다 지워버릴 수 있습니다.
# .env 파일을 사용해 안전하게 바꿔보세요.

# ❌ 위험한 코드 (비밀번호 노출)
DB_HOST = "127.0.0.1"
DB_USER = "admin"
DB_PASSWORD = "super_secret_password_1234" 

def connect_to_database():
    print("🔄 데이터베이스 접속을 시도합니다...")
    
    # 실제 접속 로직 대신 접속 정보만 출력해봅니다.
    print(f"   [접속 정보] Host: {DB_HOST}, User: {DB_USER}")
    
    # ⚠️ 비밀번호가 진짜로 코드에 적힌 값인지 확인하는 로직
    if DB_PASSWORD == "super_secret_password_1234":
        print("✅ 접속 성공! (하지만 비밀번호가 코드에 있어서 위험합니다)")
    else:
        print("❌ 접속 실패: 비밀번호 오류")

if __name__ == "__main__":
    connect_to_database()
