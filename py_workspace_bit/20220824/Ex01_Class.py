# 클래스와 객체
# 클래스의 구조
# 예시)
class FishBread:  # 클래스 선언
    def __init__(self, f, b):  # 생성자(속성) 정의
        self.flour = f  # 클래스 내에 생성자 선언 없이도 디폴트 생성자는 사용가능(자바와 동일)
        self.bean = b

    def makeFishBread(self):  # 기능(메소드, 함수) 정의
        print("붕어빵 제조")


# 클래스명은 자바와 동일하게 대문자로 시작
# 의미있는 이름으로 선언할 것
# def __init__() : 형태로 속성 정의
# self는 클래스 자신을 가리키는 의미로 첫 매개변수를 self로 지정
