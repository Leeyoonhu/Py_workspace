# 평균 구하는 함수
# 표준 입력으로 국어, 영어, 수학, 과학 점수를 입력받아 평균 점수를 실수로 출력하는 프로그램
# 반드시 total(), average() 함수 만들것

numbers = []


def total(*scores):
    total = 0
    for score in scores:
        total += score
    return total


def average(*scores):
    average = 0
    cnt = len(scores)
    return total(*scores) / cnt


num1 = int(input("국어 점수 입력 : "))
num2 = int(input("영어 점수 입력 : "))
num3 = int(input("수학 점수 입력 : "))
num4 = int(input("과학 점수 입력 : "))

print(
    "4과목의 총점은 %d, 평균은 %.1f입니다"
    % (total(num1, num2, num3, num4), average(num1, num2, num3, num4))
)
