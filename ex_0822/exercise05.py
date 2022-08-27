# 1~50 까지의 임의의 숫자를 발생하여 프로그램을 실행할 때 마다 중복되지 않는 숫자로 구성된 빙고판 생성
import random

checkList = []

while len(checkList) < 50:
    a = random.randint(1, 50)
    if a in checkList:
        a = random.randint(1, 50)
    else:
        checkList.append(a)

for i in range(1, 6):
    for j in range(1, 6):
        print(checkList.pop(), end=" ")
    print()
