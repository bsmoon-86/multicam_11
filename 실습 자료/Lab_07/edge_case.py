# [실습 3] Edge Case Debugging
# 목표: 경계값(Edge Case)에서 발생하는 버그를 찾습니다.
# 미션: AI에게 "이 코드가 실패할 수 있는 입력값(Edge Case)을 찾아줘"라고 하세요.

def get_elements(data_list, n):
    result = []
    # n이 리스트 길이보다 크거나 같으면?
    for i in range(n + 1): # <--- Off-by-one Error 의심
        result.append(data_list[i])
    return result

my_list = [10, 20, 30]
print(get_elements(my_list, 3))
