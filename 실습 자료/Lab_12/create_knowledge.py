# [실습 0] 사내 지식 베이스 생성
def create_docs():
    content = """[1조] 근무 시간
본 회사는 주 4일제(월~목)를 원칙으로 합니다. 금요일은 자율 학습일입니다.
[2조] 출장비 규정
제주도: 50만 원 / 부산: 30만 원 / 해외: 500달러
[3조] 회식 문화
저녁 회식 금지. 점심 회식 원칙.
"""
    with open("company_policy.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("company_policy.txt 생성 완료! (이 파일을 NotebookLM에 업로드하세요)")
if __name__ == "__main__": create_docs()
