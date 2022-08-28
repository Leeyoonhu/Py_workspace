# 계산기 클래스 만들기
# 클래스를 만들기 위해서는 속성과 기능을 먼저 정의


class Calc:
    def __init__(self, num1, num2):  # 속성 정의(셀프를 제외한 매개변수)
        print("=== __init__ ===")
        self.num1 = num1  # this.num1 = num1
        self.num2 = num2  # this.num2 = num2

    def add(self):
        print("=== add() start ===")
        print("num1 + num2 = %d" % (self.num1 + self.num2))

    def sub(self):
        print("=== sub() start ===")
        print("num1 - num2 = %d" % (self.num1 - self.num2))


cal1 = Calc(10, 20)  # Calc 클래스로 만든 객체 cal1
cal1.add()  # 객체의 메소드 호출
cal1.sub()

# cal1 객체의 속성 접근
print("cal1.num1 = %d" % cal1.num1)
print("cal1.num2 = %d" % cal1.num2)
