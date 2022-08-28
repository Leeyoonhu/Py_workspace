# 웹사이트 누적 방문횟수 출력프로그램
cnt = 0
while True:
    menu = int(input("1. 웹사이트 방문, 2. 종료 >> "))
    cnt += 1
    if menu == 2:
        break
    print("누적 방문 횟수 :", cnt)
