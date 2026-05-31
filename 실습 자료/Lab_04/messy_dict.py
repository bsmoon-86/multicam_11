# [실습 3] Pydantic Refactoring
# 목표: AI에게 "Pydantic을 써서 데이터 스키마를 정의하고 검증해줘"라고 요청하세요.
# (pip install pydantic 필요)

user = {
    "name": "Admin",
    "email": "invalid-email", # 이메일 형식이 아님
    "age": "서른" # 숫자가 아님
}

def create_user(u):
    print(f"User {u['name']} created.")

if __name__ == "__main__":
    create_user(user)
