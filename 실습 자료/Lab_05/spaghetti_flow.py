# [실습 3] 로직 시각화 (Flowchart)
# 상황: 조건문이 너무 깊어서(Nested) 머릿속으로 흐름을 그리기 어렵습니다.
# 미션: AI에게 "이 함수의 로직 흐름을 Mermaid Flowchart 코드로 작성해줘"라고 요청하세요.
# (팁: 생성된 코드를 https://mermaid.live 에 붙여넣어 확인하세요)

def process_approval(doc_type, amount, approver_rank):
    status = "PENDING"
    if doc_type == "EXPENSE":
        if amount < 100000:
            status = "APPROVED_AUTO"
        else:
            if approver_rank == "MANAGER":
                status = "APPROVED_MANAGER"
            elif approver_rank == "DIRECTOR":
                status = "APPROVED_DIRECTOR"
            else:
                status = "REJECTED_LOW_RANK"
    elif doc_type == "VACATION":
        if approver_rank == "HR":
            status = "APPROVED_HR"
        else:
            status = "WAITING_HR"
    
    return status
