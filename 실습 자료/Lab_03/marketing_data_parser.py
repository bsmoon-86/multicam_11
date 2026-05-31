import os

def parse_marketing_data(file_path: str) -> list[dict]:
    parsed_data = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    # 1. 헤더 줄 찾기 (주석 건너뛰기)
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith("name"):
            start_idx = i
            break
            
    # 2. 헤더 파싱: 혼용된 구분자(콤마, 탭)를 파이프(|)로 통일 후 분리
    header_line = lines[start_idx]
    # replace를 연속 호출하여 구분자 통일 -> split으로 자르기 -> 리스트 내포로 공백 제거
    headers = [h.strip() for h in header_line.replace(',', '|').replace('\t', '|').split('|')]
    
    # 3. 데이터 파싱
    for line in lines[start_idx + 1:]:
        line = line.strip()
        if not line:  # 빈 줄 건너뛰기
            continue
            
        values = [v.strip() for v in line.replace(',', '|').replace('\t', '|').split('|')]
        
        # 4. 헤더와 값을 매핑하여 딕셔너리 생성
        row_dict = {}
        for i in range(len(headers)):
            # 데이터가 누락된 경우(예: Park의 전화번호)를 대비한 예외 처리
            row_dict[headers[i]] = values[i] if i < len(values) else ""
            
        parsed_data.append(row_dict)
        
    return parsed_data

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "marketing_data.txt")
    result = parse_marketing_data(file_path)
    
    print("🚀 파싱된 리스트 딕셔너리 결과:")
    for item in result:
        print(item)