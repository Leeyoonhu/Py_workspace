calc, num1, num2 = "", 0, 0

print("두 숫자를 입력하세요")
num1, num2 = int(input()), int(input())
calc = input("사용하실 연산자를 입력하세요(+, -, *, //) : ")

if calc == "+":
    print("%d" % (num1 + num2))
elif calc == "-":
    print("%d" % (num1 - num2))
elif calc == "//":
    print("%d" % (num1 // num2))
elif calc == "*":
    print("%d" % (num1 * num2))
else:
    print("연산자만 입력해주세요.")
print("사칙 연산 종료")
