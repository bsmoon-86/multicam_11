# [실습 4] 구조 시각화 (Class Diagram)
# 상황: 여러 클래스가 상속 관계로 얽혀 있어 구조 파악이 어렵습니다.
# 미션: AI에게 "이 클래스들의 상속 및 관계를 Mermaid Class Diagram으로 그려줘"라고 요청하세요.

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Playable(Character):
    def attack(self):
        pass

class NPC(Character):
    def talk(self):
        pass

class Warrior(Playable):
    def attack(self):
        print("Sword Attack")

class Mage(Playable):
    def attack(self):
        print("Magic Ball")

class Merchant(NPC):
    def trade(self):
        print("Buying/Selling")
