# 여러 모듈을 import 받은 상태
# 해당 모듈들이 자동실행되는 출력문이 있다고 가정
# import만 해도 실행될 때 각 모듈에__name__ 전역변수 사용
# __name__ 전역 변수는 실행하는 py파일에서는 main으로 나타나고, import한 애들은 이름으로 나타남
# 따라서
#   if __name__ == "__main__":
#   == 자동 출력 함수 ==
#   print("__name__:", __name__)
