class Car:
    color = ""
    speed = 0
    count = 0

    def __init__(self):  # 생성자 사용시마다 카운트 1씩 증가
        self.speed = 0
        Car.count += 1


myCar1 = Car()
myCar1.speed = 30
print("자동차1 : 현재 속도는 %dkm, 생산된 자동차는 총 %d대 입니다." % (myCar1.speed, Car.count))

myCar2 = Car()
myCar2.speed = 60
print("자동차2 : 현재 속도는 %dkm, 생산된 자동차는 총 %d대 입니다." % (myCar2.speed, Car.count))
