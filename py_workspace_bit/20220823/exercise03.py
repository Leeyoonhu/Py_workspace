# 웹사이트 방문 여부를 입력받아 누적 방문횟수 출력 프로그램
count = 1
while True:
    choice = int(input("1.웹사이트 방문, 2.종료 >> "))
    if choice == 1:
        print("누적 방문 횟수 : %d" % count)
        count += 1
    if choice == 2:
        break
