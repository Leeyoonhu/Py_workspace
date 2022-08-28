# 시작, 끝단 받아서 출력하는 구구단 프로그램

num1 = int(input("구구단의 시작단 입력 : "))
num2 = int(input("구구단의 끝단 입력 : "))
for i in range(1, 10):
    if num1 > num2:
        for j in range(num1, num2 - 1, -1):
            print(str(j) + "*" + str(i) + "=", j * i, end=" ")
        print()
    for j in range(num1, num2 + 1, 1):
        print(str(j) + "*" + str(i) + "=", j * i, end=" ")
    print()
