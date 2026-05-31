# [실습 1] SQL Injection
# 미션: "이 코드를 공격할 수 있는 Payload를 알려주고, 안전하게(Parameterized) 고쳐줘."
import sqlite3

def login(username, password):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'admin', 'super_secret')")
    
    # ⚠️ 위험!
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Query: {query}")
    cursor.execute(query)
    
    if cursor.fetchone(): print("Login Success!")
    else: print("Login Failed.")

login("admin", "wrong_pass") # 실패
# 공격 예시: login("admin' --", "anything")
