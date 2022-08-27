# 로또는 언제 당첨될까?
# 중복되지않는 1~45 두 놈끼리 계속 굴려서.. 모든 수가 같을때 스탑
import random

lottoSet1 = set()
lottoSet2 = set()
cnt = 0
while True:
    while True:
        lottoSet1.add(random.randint(1, 45))
        if len(lottoSet1) == 6:
            break

    while True:
        lottoSet2.add(random.randint(1, 45))
        if len(lottoSet2) == 6:
            break
    cnt += 1
    lottoList1 = list(lottoSet1)
    lottoList2 = list(lottoSet2)

    print("%d회 당첨 로또번호 : " % cnt, lottoList1)
    print("당신이 뽑은 로또번호 : ", lottoList2)

    if lottoSet1 == lottoSet2:
        break
    else:
        lottoSet1.clear()
        lottoSet2.clear()


print("축하합니다. 이번주 로또 당첨번호는 ==> %d\n 당첨 되기까지 구매 횟수는 %d회 입니다." % (lottoList1, cnt))
