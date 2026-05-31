# [실습 1] Decorator Refactoring
# 목표: AI에게 "AOP 패턴을 적용해 로깅 로직을 분리해줘"라고 요청하세요.
import time

def process_A():
    print("--- START ---")
    start = time.time()
    time.sleep(1)
    end = time.time()
    print(f"--- END (Time: {end-start:.2f}s) ---")

def process_B():
    print("--- START ---")
    start = time.time()
    time.sleep(0.5)
    end = time.time()
    print(f"--- END (Time: {end-start:.2f}s) ---")

if __name__ == "__main__":
    process_A()
    process_B()
