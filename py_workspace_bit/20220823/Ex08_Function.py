# return 의 또다른 기능
# 함수를 종료시키고, 프로그램을 호출부로 보냄


def increaseStar():
    print("*")
    print("**")
    print("***")
    return
    print("*")  # 호출부
    print("**")
    print("***")


increaseStar()
