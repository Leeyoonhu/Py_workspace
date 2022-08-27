# 1~50 까지의 임의의 숫자를 발생하여 프로그램을 실행할 때 마다 중복되지 않는 숫자로 구성된 5*5 빙고판 생성
import random

randSet = set()
while True:
    randSet.add(random.randint(1, 50))
    if len(randSet) >= 25:
        break

randList = list(randSet)
random.shuffle(randList)

for i in range(1, 26):
    print(randList[i - 1], end=" ")
    if i % 5 == 0 and i != 0:
        print()
