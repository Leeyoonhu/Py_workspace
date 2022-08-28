class Car:
    def __init__(self):  # 디폴트 생성자
        self.color = "빨강"
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


myCar1 = Car()
myCar2 = Car()

print("myCar1 의 색상은 %s 이며, 속도는 %d km입니다." % (myCar1.color, myCar1.speed))
print("myCar2 의 색상은 %s 이며, 속도는 %d km입니다." % (myCar2.color, myCar2.speed))
