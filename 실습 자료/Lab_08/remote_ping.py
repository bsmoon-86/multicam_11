# [실습 2] Command Injection
# 미션: "이 코드의 위험성을 설명하고, subprocess 모듈로 안전하게 바꿔줘."
import os

def check_server(ip):
    # ⚠️ 위험! 사용자가 "8.8.8.8; rm -rf /" 입력 시 실행됨
    cmd = "ping -c 1 " + ip
    os.system(cmd)

ip = input("IP: ")
check_server(ip)
