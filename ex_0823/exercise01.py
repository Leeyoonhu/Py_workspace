# 입력한 수의 각 자릿수 2배만큼 * 출력 프로그램 작성
numlist = []
numbers = int(input("숫자를 여러 개 입력하세요 : "))
numlist.append((numbers // 1000) * 2)
numlist.append(((numbers // 100) % 10) * 2)
numlist.append(((numbers // 10) % 10) * 2)
numlist.append((numbers % 10) * 2)
print()

i = 0
while i < 4:
    for j in range(numlist[i]):
        print("*", end="")
    print()
    i += 1
