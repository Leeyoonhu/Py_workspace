# 함수 => 매개변수를 입력받은 후, 가공하고 처리하여 반환값을 돌려줌
# 장점) 필요할때 호출, 논리적 단위 분할, 코드의 캡슐화
# def funcName (parameter1,...):
#   실행문 1
#   실행문 2
#   return 반환값
# fucntionName에는 행위를 기록하므로 동사와 명사를 함께 사용 ex) find_numbers
# 주의) 함수를 작성하기 전에 먼저 호출하면 안됨

# 예시) 두 정수를 입력받아 두 정수의 합계를 반환하는 함수


def add(v1, v2):  # 함수 선언
    result = 0  # 실행문 1
    result = v1 + v2  # 실행문 2
    return result  # return 반환값


sum = 0
sum = add(100, 200)  # 함수 사용(호출)
print("%d과 %d의 add()함수 결과는 %d" % (100, 200, sum))
