# while 조건식 : 반복 실행문, 변화식
# 반복문 사용 전에 어떤게 반복되야할지 확실히 판별할 것
# 예제)
i = 0
while i < 5:
    print("Hello World%d" % i)  # 반복 실행문
    i += 1  # 변화식

# 1~10까지의 합
i = 0
sum = 0
while i < 11:
    sum += i
    i += 1
print("1부터 10까지의 합 : %d" % sum)

# 입력받은 두 수의 합을 계산하는 프로그램 (무한루프) - 종료시 ctrl+c
while True:
    num1 = int(input("첫번째 숫자 입력 : "))
    num2 = int(input("두번째 숫자 입력 : "))
    print("%d + %d = %d" % (num1, num2, (num1 + num2)))
