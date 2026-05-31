# [실습 3] Edge Case Discovery
# 상황: 재고 관리 로직입니다. 평범해 보이지만 구멍이 많습니다.
# 미션: AI에게 "이 코드를 망가뜨릴 수 있는 엣지 케이스를 찾고, 이를 검증하는 테스트를 짜줘"라고 하세요.

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name not in self.items:
            self.items[name] = 0
        self.items[name] += quantity

    def remove_item(self, name, quantity):
        # 버그: 재고보다 많이 빼면 음수가 됩니다!
        if name in self.items:
            self.items[name] -= quantity
