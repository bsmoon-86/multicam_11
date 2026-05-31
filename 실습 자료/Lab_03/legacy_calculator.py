# [실습 1] Persona & Structure
# 목표: 절차지향 코드를 "객체지향(OOP) + SOLID 원칙"이 적용된 구조로 변경하세요.
# Bad Prompt: "이거 리팩토링해줘" (단순 함수화)
# Good Prompt: "너는 SW 아키텍트야. 추상 클래스(ABC)를 사용하여 확장 가능한 구조로 바꾸고, SOLID 원칙을 적용해줘."

from abc import ABC, abstractmethod

# 1. 인터페이스 (추상 클래스) 정의
class Operation(ABC):
    @abstractmethod
    def calculate(self, n1: float, n2: float) -> float:
        pass

# 2. 구체적인 연산 클래스들 (각자 하나의 연산에만 책임)
class Addition(Operation):
    def calculate(self, n1: float, n2: float) -> float:
        return n1 + n2

class Subtraction(Operation):
    def calculate(self, n1: float, n2: float) -> float:
        return n1 - n2

class Multiplication(Operation):
    def calculate(self, n1: float, n2: float) -> float:
        return n1 * n2

class Division(Operation):
    def calculate(self, n1: float, n2: float) -> float:
        if n2 == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return n1 / n2

# 3. Calculator 클래스 (Context) - OCP 준수
class Calculator:
    def __init__(self):
        self._operations = {}

    def register_operation(self, symbol: str, operation: Operation):
        self._operations[symbol] = operation

    def execute(self, symbol: str, n1: float, n2: float) -> float:
        operation = self._operations.get(symbol)
        if not operation:
            raise ValueError(f"지원하지 않는 연산자입니다: '{symbol}'")
        return operation.calculate(n1, n2)

if __name__ == "__main__":
    # 계산기 인스턴스 생성 및 연산자 등록 (DI)
    calc = Calculator()
    calc.register_operation('+', Addition())
    calc.register_operation('-', Subtraction())
    calc.register_operation('*', Multiplication())
    calc.register_operation('/', Division())

    try:
        op = input("연산자(+, -, *, /): ")
        n1 = float(input("숫자1: "))
        n2 = float(input("숫자2: "))
        print(f"결과: {calc.execute(op, n1, n2)}")
    except Exception as e:
        print(f"에러: {e}")
