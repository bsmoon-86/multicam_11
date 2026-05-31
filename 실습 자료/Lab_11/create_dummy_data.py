# [실습 준비] 더미 데이터 생성기
# 이 파일을 먼저 실행해서 'sales_data.csv'를 만들어야 합니다.
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def create_data():
    rows = 1000
    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
    cities = ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Seoull', 'Pusan'] # 오타 포함
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for _ in range(rows):
        date = start_date + timedelta(days=random.randint(0, 365))
        product = random.choice(products)
        city = random.choice(cities)
        price = random.randint(10000, 2000000)
        quantity = random.randint(1, 5)
        
        # 10% 확률로 결측치(NaN) 생성
        if random.random() < 0.1:
            price = None
            
        data.append([date, product, city, price, quantity])
        
    df = pd.DataFrame(data, columns=['Date', 'Product', 'City', 'Price', 'Quantity'])
    df.to_csv('sales_data.csv', index=False)
    print("sales_data.csv 생성 완료!")

if __name__ == "__main__":
    create_data()
