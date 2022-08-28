# 로또 번호 생성기
import random


def getNumber():
    return random.randint(1, 45)


lotto = []
num = 0

while True:
    num = getNumber()  # 난수 뽑기
    if lotto.count(num) == 0:  # lotto배열에 해당 난수 카운트가 0일경우
        lotto.append(num)  # lotto 배열에 난수 추가
    if len(lotto) >= 6:  # lotto 배열의 길이가 6이상이면
        break  # 무한루프 탈출

print("추첨된 로또 번호 ==> ", end="")
lotto.sort()  # lotto 배열 정렬
for i in range(len(lotto)):
    print("%d " % lotto[i], end="")
