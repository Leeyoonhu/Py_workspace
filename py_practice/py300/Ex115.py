# 입력받은 값의 20빼기, 단 출력범위 0~255 // 0보다 작을경우 0출력, 255보다 클경우 255
num = int(input(">> 입력값: "))
num2 =  num - 20
print("출력값: ", end="")
if 0 <= num2 <= 255:
    print(num2)
if num2 < 0:
    print(0)
if num2 > 255:
    print(255)