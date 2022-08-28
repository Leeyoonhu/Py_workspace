# 부모클래스와 자식클래스가 동일한 파일에 있을경우
# from 부모위치 import 부모클래스명을 적지 않음
# 자바처럼 자식클래스가 메소드 오버라이딩 가능함


class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value
        print("현재 속도(부모/슈퍼 클래스) : %d" % self.speed)


class Sedan(Car):  # Car 클래스를 상속받은 Sedan 클래스
    def upSpeed(self, value):  # 부모 메서드 오버라이딩
        self.speed += value
        if self.speed > 150:
            self.speed = 150
            print("현재 속도(자식/서브 클래스) : %d" % self.speed)


class Truck(Car):  # Car 클래스를 상속받은 Truck 클래스
    pass  # 예약어 pass 사용


truck1 = Truck()
sedan1 = Sedan()

print("트럭 --> ", end=" ")
truck1.upSpeed(200)  # 트럭 클래스 내에서 해당 메소드 오버라이딩 하지 않았으므로 부모 클래스 메서드 사용

print("승용차 --> ", end=" ")
sedan1.upSpeed(200)  # 세단 클래스 내에서 오버라이딩 한 조건을 통해 속도 150으로 고정
