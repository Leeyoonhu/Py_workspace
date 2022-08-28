# 반환값과 매개변수 // 반드시 반환값이 있어야하는것은 아니며, *반환값도 1개이상 가능(list,dictionary..etc)*
# 예시)
def function1():
    result = 10
    return result  # 반환 값 1개 리턴


def function2():
    print("반환값이 없는 함수 실행")  # 반환값이 없는 함수


print("function1() 에서 반환한 값 : %d" % function1())
function2()
