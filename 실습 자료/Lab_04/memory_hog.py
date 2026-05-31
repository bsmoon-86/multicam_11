# [실습 2] Generator Refactoring
# 목표: AI에게 "Lazy Evaluation을 적용해 메모리를 최적화해줘"라고 요청하세요.
import sys

def heavy_process():
    # 100만 개를 리스트에 다 담음 (메모리 낭비)
    data = []
    for i in range(1000000):
        data.append(i)
    return data

if __name__ == "__main__":
    result = heavy_process()
    print(f"Size: {sys.getsizeof(result)/1024/1024:.2f} MB")
