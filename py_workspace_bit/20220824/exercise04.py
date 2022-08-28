# 사용자가 1부터 45까지 정수 6개 입력
# 컴퓨터에서는 1부터 45까지 난수 6개를 발생하여
# 비교해서 일치하는 숫자 출력 프로그램 작성
import random

lottoSet = set()
while True:
    lottoSet.add(random.randint(1, 45))
    if len(lottoSet) == 6:
        break
lottoList = list(lottoSet)
random.shuffle(lottoList)
numList = []
sameList = []
print("1 부터 45까지의 정수 6개를 입력하세요.")
for i in range(len(lottoList)):
    numList.append(int(input("Number " + str(i + 1) + ": ")))
print("이번주 로또 번호", lottoList)
print("내가 선택한 번호", numList)
for lottoNum in lottoList:
    if lottoNum in numList:
        sameList.append(lottoNum)

print("일치하는 숫자 :", sameList)
