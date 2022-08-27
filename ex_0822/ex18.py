# 조건문(if, else, elif)
# if 조건식 : 실행문, 들여쓰기(indentation) 위치가 중요함(조건식의 몸체를 들여쓰기 위치로 판단)
from time import process_time_ns


x = 10
if x == 10:
    print("10 입니다")
else:
    print("10이 아닙니다")
print("x = %d" % x)  # 들여쓰기 위치가 다르기때문에 조건식의 실행문으로 보지않고 그냥 print문으로 인식

number = int(input("숫자를 입력하세요 : "))
if number % 2 == 0:
    print("입력하신 숫자는 짝수입니다")
else:
    print("입력하신 숫자는 홀수입니다")
