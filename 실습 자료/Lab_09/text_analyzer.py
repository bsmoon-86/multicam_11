# [실습 2] 파라미터화 테스트 생성
# 상황: 다양한 입력값에 대해 로직이 잘 도는지 확인해야 합니다.
# 미션: AI에게 "@pytest.mark.parametrize를 사용해서 5가지 이상의 문장을 테스트해줘"라고 하세요.

def count_words(text):
    if not text:
        return 0
    # 공백 기준으로 단어 분리
    words = text.strip().split()
    return len(words)

def extract_hashtags(text):
    # #으로 시작하는 단어 추출
    return [word for word in text.split() if word.startswith("#")]
