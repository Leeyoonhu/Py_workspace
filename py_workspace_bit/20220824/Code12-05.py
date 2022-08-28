class Car:
    name = ""
    speed = 0

    def __init__(self, name, speed):  # 디폴트 생성자
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed


car1, car2 = Car("아우디", 0), Car("벤츠", 30)

print("car1 의 이름은 %s 이며, 속도는 %d km입니다." % (car1.getName(), car1.getSpeed()))
print("car2 의 이름은 %s 이며, 속도는 %d km입니다." % (car2.getName(), car2.getSpeed()))
