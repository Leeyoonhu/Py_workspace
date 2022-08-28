# 계산기 함수 만들기
def calc(num1, num2, operator):
    result = 0
    if operator == "+":
        result = num1 + num2
    if operator == "-":
        result = num1 - num2
    if operator == "*":
        result = num1 * num2
    if operator == "/":
        result = int(num1 / num2)
    return result


num1 = int(input("첫번째 숫자를 입력하세요 : "))
operator = input("연산자를 입력하세요 : ")
num2 = int(input("두번째 숫자를 입력하세요 : "))
print("%d %s %d = %d" % (num1, operator, num2, calc(num1, num2, operator)))
