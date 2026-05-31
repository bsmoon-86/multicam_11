import json
import re
from datetime import datetime

# [실습 3] Format Control
# 목표: 까다로운 규칙을 준수하는 JSON 데이터를 생성하세요.
# Bad Prompt: "이 데이터로 JSON 만들어줘"
# Good Prompt: "결과를 JSON으로 출력하되, 1) 모든 Key는 snake_case, 2) 전화번호 없으면 'N/A', 3) 날짜는 YYYY-MM-DD 형식으로 변환해."

users = [
    {"Name": "Alice", "Phone": "010-1234-5678", "JoinedAt": "2024.01.01"},
    {"Name": "Bob", "Phone": None, "JoinedAt": "2024/02/15"},
    {"Name": "Charlie", "Phone": "010-9876-5432", "JoinedAt": "2024-03-10"}
]

def to_snake_case(name):
    """CamelCase 또는 PascalCase 문자열을 snake_case로 변환합니다."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def generate_custom_json(data):
    processed_data = []
    
    for item in data:
        if not isinstance(item, dict):
            raise TypeError(f"유효하지 않은 데이터 형식입니다 (dict 필요): {type(item)}")
            
        processed_item = {}
        for key, value in item.items():
            # 1. 모든 Key를 snake_case로 변환
            snake_key = to_snake_case(key)
            
            # 2. 결측치(None 또는 빈 문자열) 처리
            if value is None or str(value).strip() == "":
                processed_item[snake_key] = "N/A"
                continue
                
            # 3. 날짜 ISO 8601 변환 및 정합성 검증
            if snake_key == "joined_at":
                # 다양한 기호(., /)를 하이픈(-)으로 통일
                normalized_date = re.sub(r'[./]', '-', str(value))
                try:
                    # 실제 존재하는 날짜인지 검증 후 지정 포맷으로 변환
                    valid_date = datetime.strptime(normalized_date, "%Y-%m-%d")
                    processed_item[snake_key] = valid_date.strftime("%Y-%m-%d")
                except ValueError:
                    raise ValueError(f"유효하지 않은 날짜 포맷입니다 ({key}: {value}). 올바른 연/월/일인지 확인하세요.")
            else:
                processed_item[snake_key] = value
                
        processed_data.append(processed_item)
        
    return json.dumps(processed_data, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # 결과 테스트
    result_json = generate_custom_json(users)
    print("🚀 생성된 커스텀 JSON 결과:")
    print(result_json)
