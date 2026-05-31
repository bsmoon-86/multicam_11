# [실습 4] Instruction & Security (CoT)
# 목표: SQL Injection 취약점을 단계별로 분석하고 안전하게 수정하세요.
# Bad Prompt: "이 코드 좀 다듬어줘" (취약점 못 찾고 스타일만 바꿈)
# Good Prompt: "너는 보안 감사관이야. 다음 단계로 진행해. 1) 취약점 분석, 2) 공격 시나리오 예상, 3) Parameterized Query를 적용한 수정 코드 작성."

def get_user_info(user_id):
    # ⚠️ 위험! 사용자가 "1 OR 1=1"을 입력하면 모든 정보가 털립니다.
    sql = f"SELECT * FROM users WHERE id = '{user_id}'"
    print(f"Executing: {sql}")
    # cursor.execute(sql) ... (생략)

# 테스트
get_user_info("admin' --") 
