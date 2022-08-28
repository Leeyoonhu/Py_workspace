def func():
    print("module01 함수 실행")
    print("__name__", __name__)


if __name__ == "__main__":
    func()
    print("__name__:", __name__)
