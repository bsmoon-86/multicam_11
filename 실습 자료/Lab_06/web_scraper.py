# [실습 2] README Generation
# 미션: AI에게 "설치법(pip)과 사용법이 포함된 README.md를 작성해줘"라고 요청하세요.
import requests
from bs4 import BeautifulSoup
import sys

def get_title(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.title.string
    except:
        return "Error"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python web_scraper.py <url>")
    else:
        print(get_title(sys.argv[1]))
