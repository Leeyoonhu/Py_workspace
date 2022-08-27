# 시작단과 끝단을 입력받아 출력하는 프로그램
# 시작단이 끝단보다 높을경우, 역순으로

sDan = int(input("구구단의 시작단 입력 : "))
eDan = int(input("구구단의 끝단 입력 : "))

if sDan < eDan:
    for i in range(1, 10):
        for j in range(sDan, (eDan + 1)):
            print("%d*%d=%2d" % (j, i, j * i), end=" ")
        print()
else:
    for i in range(1, 10):
        for j in range(sDan, (eDan - 1), -1):
            print("%d*%d=%2d" % (j, i, j * i), end=" ")
        print()
