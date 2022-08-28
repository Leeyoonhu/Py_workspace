# 클래스의 속성(변수)는 모든 인스턴스가 공유


class Person:
    pocket = []  # 클래스 속성(변수)

    def put_pocket(self, value):
        self.pocket.append(value)


conan = Person()  # Person 클래스의 객체 conan
conan.put_pocket("스마트폰")  # pocket에 스마트폰 추가

rose = Person()
rose.put_pocket("책")  # pocket에 책 추가

# 모든 인스턴스 공유 확인
print("conan :", conan.pocket)
print("rose :", rose.pocket)
print("Person :", Person.pocket)

# 만약에 공유하지않고 객체마다 따로 저장하려면


class Reperson(Person):
    def put_pocket(self, myPocket, value):  # 생성자에 파라미터 추가
        self.pocket = myPocket
        self.pocket.append(value)


conan = Reperson()
conan.pocket = []
conan.put_pocket(conan.pocket, "스마트폰")

rose = Reperson()
rose.pocket = []
rose.put_pocket(rose.pocket, "책")
print("conan :", conan.pocket)
print("rose :", rose.pocket)
