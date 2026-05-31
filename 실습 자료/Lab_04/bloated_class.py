# [실습 4] Dataclass Refactoring
# 목표: AI에게 "Dataclass를 사용해서 보일러플레이트 코드를 제거해줘"라고 요청하세요.

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price})"
    
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

if __name__ == "__main__":
    i1 = Item("Mouse", 1000)
    print(i1)
