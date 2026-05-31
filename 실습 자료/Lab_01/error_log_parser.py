import csv
import re
import logging
from pathlib import Path

# 로깅 설정: 시니어 개발자는 print 대신 logging 모듈을 즐겨 사용합니다.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ErrorLogExtractor:
    """
    비정형 서버 로그 파일에서 특정 레벨(ERROR)의 로그만 추출하여 
    CSV 형태의 정형 데이터로 변환하는 데이터 파이프라인 클래스입니다.
    """
    
    def __init__(self, input_path: str, output_path: str):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        
        # 정규표현식: [YYYY-MM-DD HH:MM:SS] [LEVEL] 메시지 형태를 정확하게 그룹핑하여 추출
        self.log_pattern = re.compile(
            r"^\[(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\]\s\[(?P<level>[A-Z]+)\]\s(?P<message>.*)$"
        )

    def process_logs(self) -> None:
        """전체 프로세스 실행 (읽기 -> 필터링 및 파싱 -> CSV 저장)"""
        if not self.input_path.exists():
            logger.error(f"로그 파일을 찾을 수 없습니다: {self.input_path}")
            return
            
        error_data = self._extract_error_logs()
        self._save_to_csv(error_data)

    def _extract_error_logs(self) -> list[dict]:
        """파일을 한 줄씩 읽으며 정규표현식으로 파싱하고 ERROR 레벨만 수집합니다."""
        extracted = []
        
        with open(self.input_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = self.log_pattern.match(line.strip())
                # 매칭에 성공하고, 해당 로그의 레벨이 'ERROR'인 경우만 적재
                if match and match.group('level') == 'ERROR':
                    extracted.append({
                        'Date': match.group('date'),
                        'Time': match.group('time'),
                        'Message': match.group('message')
                    })
                    
        logger.info(f"총 {len(extracted)}건의 ERROR 로그를 성공적으로 추출했습니다.")
        return extracted

    def _save_to_csv(self, data: list[dict]) -> None:
        """추출된 리스트 데이터를 지정된 경로의 CSV로 저장합니다."""
        if not data:
            logger.warning("추출된 ERROR 로그가 없어 CSV 파일을 생성하지 않습니다.")
            return
            
        with open(self.output_path, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Date', 'Time', 'Message'])
            writer.writeheader()
            writer.writerows(data)
            
        logger.info(f"ERROR 데이터가 성공적으로 저장되었습니다: {self.output_path}")

if __name__ == "__main__":
    # 클래스 실행
    BASE_DIR = Path(r"c:\Users\ekfla\Documents\GitHub\multicam_11\실습 자료\Lab_01")
    extractor = ErrorLogExtractor(
        input_path=BASE_DIR / "server_logs.txt",
        output_path=BASE_DIR / "error_logs.csv"
    )
    extractor.process_logs()