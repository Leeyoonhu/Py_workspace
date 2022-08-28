# 빙고판 생성하기
# 1~50 숫자를 발생시켜 프로그램 실행시마다 랜덤한 숫자로 구성된 빙고판
import random

randSet = set()
while True:
    randSet.add(random.randint(1, 50))
    if len(randSet) == 25:
        break

randList = list(randSet)
random.shuffle(randList)
cnt = 0
for randNum in randList:
    print(randNum, end=" ")
    cnt += 1
    if cnt == 5:
        cnt = 0
        print()
