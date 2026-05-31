# 1차시 2교시 실습 가이드 (Safe Coding)

이 실습은 실제 API Key 없이도 안전한 보안 습관을 기를 수 있도록 구성되었습니다.

## 🛠️ 준비
`pip install python-dotenv`

## 🚀 실습 1: DB 비밀번호 숨기기
1. `unsafe_db.py`를 실행해보고 비밀번호가 노출된 것을 확인합니다.
2. `.env` 파일을 만들고 
   - `DB_HOST=127.0.0.1` -
   - `DB_USER=admin`
   - `DB_PASSWORD=super_secret_password_1234`
   를 적습니다.
3. 코드를 수정합니다:
   - `import os`, `from dotenv import load_dotenv`
   - `load_dotenv()`
   - `DB_HOST = os.getenv("DB_HOST")`
   - `DB_USER = os.getenv("DB_USER")`
   - `DB_PASSWORD = os.getenv("DB_PASSWORD")`
4. 다시 실행해서 접속이 성공하는지 확인합니다.

## 🚀 실습 2: 개인정보 마스킹
1. Gemini Code Assist를 켭니다.
2. "파이썬 re 모듈을 써서 텍스트 안의 '휴대폰 번호'와 '이메일'을 찾아서 각각 '[PHONE]', '[EMAIL]'로 치환하는 함수를 짜줘."라고 물어봅니다.
3. AI가 준 코드를 적용합니다.
