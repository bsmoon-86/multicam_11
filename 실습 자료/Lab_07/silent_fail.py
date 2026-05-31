# [실습 4] Silent Failure Debugging
# 목표: 에러를 삼키는 나쁜 패턴을 찾아 로깅을 추가합니다.
# 미션: AI에게 "왜 아무 출력이 없는지, logging을 추가해서 원인을 찾아줘"라고 하세요.

def process_transaction(amount):
    try:
        if amount < 0:
            raise ValueError("Negative amount")
        
        result = 100 / amount
        print(f"Processed: {result}")
        
    except Exception:
        # 에러를 무시함 (Silent Failure)
        pass 

process_transaction(0)
print("Finished.")
