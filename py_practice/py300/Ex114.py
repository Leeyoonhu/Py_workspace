# 입력받은 수에 20더하기, 단 출력값이 255 초과시 255만출력
num = int(input(">> 입력값: "))
num2 = num + 20
if num2 <= 255:
    print("출력값: %d" %num2)
else :
    print("출력값: %d" %255)