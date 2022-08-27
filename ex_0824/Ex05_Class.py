# 비공개 클래스 속성


class Knight:
    __item__limit = 10  # 비공개 속성(변수, attribute, variable...)

    def print_item_limit(self):
        print(Knight.__item__limit)


x = Knight()  # Knight 객체 x 생성
x.print_item_limit()  # 객체의 함수 호출을 통해서 불러오는 것은 가능

print(Knight.__item__limit)  # 직접적인 호출은 불가능 // Java 의 private 변수와 동일한 개념
# 실행 시 Knight 클래스 안에 해당 속성을 찾을수 없음 // Java는 invisible
