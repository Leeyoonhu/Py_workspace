# 클래스의 상속
# 현재 경우는 부모클래스와 자식클래스가 다른파일에 있을경우임
from Ex02_Class import Calc  # from py위치 import 클래스명


class advancedCalc(Calc):  # class 클래스명(부모클래스)
    def pow(self):
        print("=== pow() start ===")
        print("num1 ^ num2 = %d" % (self.num1**self.num2))


cal2 = advancedCalc(10, 3)
cal2.add()  # 부모 클래스의 기능(함수, 메서드) 사용
cal2.sub()
cal2.pow()  # 자식 클래스에서 생성한 기능(함수, 메서드) 사용
