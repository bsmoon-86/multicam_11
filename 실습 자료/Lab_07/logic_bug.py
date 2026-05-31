# [실습 1] Logic Error Debugging
# 목표: 0점을 제외하고 평균을 구해야 하는데, 결과가 이상합니다.
# 미션: AI에게 "논리적 오류를 찾아서 수정해줘"라고 하세요.

def calculate_average(scores):
    total = 0
    count = 0
    for score in scores:
        if score == 0:
            # 0점은 제외하려고 했으나... continue 위치나 로직이 맞을까요?
            print("Skipping zero")
        
        total += score
        count += 1
    
    if count == 0: return 0
    return total / count

class_scores = [80, 90, 0, 100]
print(f"Result: {calculate_average(class_scores)}") 
# 예상: (80+90+100)/3 = 90
