# 입력한 수의 각 자릿수 2배만큼 * 출력 프로그램 작성

str = input("0이상 수를 입력하세요 >> ")

for i in range(len(str)):
    for j in range((2 * int(str[i]))):
        print("*", end="")
    print()
