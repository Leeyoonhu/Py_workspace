# 지역변수와 전역변수
def function1():
    a = 10  # 지역변수
    print("function1()에서 a = %d" % a)


def function2():
    print("function2()에서 a = %d" % a)


a = 20  # 전역변수

function1()
function2()
