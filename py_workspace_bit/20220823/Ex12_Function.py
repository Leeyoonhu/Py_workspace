# 함수 내에서 전역변수 재설정
def function1():
    global a  # 전역변수 재설정(이 함수 안에서의 a는 전역변수)
    a = 10
    print("function1()에서 a = %d" % a)


def function2():
    print("function2()에서 a = %d" % a)


a = 20  # 전역변수
function1()
function2()

# pass 예약어

if True:
    pass
else:
    print("false")
