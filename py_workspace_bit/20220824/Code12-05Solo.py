class Car:
    name, color, speed = "", "", 0

    def __init__(self):
        self.name
        self.color
        self.speed

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

    def getColor(self):
        return self.color

    def setColor(self, value):
        self.color = value

    def getSpeed(self):
        return self.speed

    def setSpeed(self, value):
        self.speed = value


superCar = Car()
print(
    "현재 차의 이름은 %s, 색상은 %s, 속도는 %dkm 입니다."
    % (superCar.getName(), superCar.getColor(), superCar.getSpeed())
)

superCar.setName("아우디")
superCar.setColor("빨강")
superCar.setSpeed(100)

print(
    "현재 차의 이름은 %s, 색상은 %s, 속도는 %dkm 입니다."
    % (superCar.getName(), superCar.getColor(), superCar.getSpeed())
)
