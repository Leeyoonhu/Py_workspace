# 물건값과 손님이 지불한 금액을 입력받아 거스름돈 계산 출력 프로그램
from operator import concat


price = input("물건값 입력 : ")
money = input("지불액 입력 : ")
result = int(money) - int(price)
a = str(result // 5000)
b = str(result % 5000 // 1000)
c = str(result % 1000 // 500)
d = str(result % 500 // 100)
e = str(result % 100 // 50)
f = str(result % 50 // 10)
print(
    "거스름돈은 "
    + str(result)
    + "원이며, 5000원권 "
    + a
    + " ,1000원권\n "
    + b
    + "개, 500원짜리 " 
    + c
    + "개, 100원짜리 "
    + d
    + "개, 50원짜리 "
    + e
    + "개\n, 10원짜리 "
    + f
    + "개임",
)
