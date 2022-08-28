#  입력받은 내용이 리스트 안에있는지 확인하기
fruit = ["사과", "포도", "홍시"]
choice = input(">> 좋아하는 과일은? ")
if choice in fruit:
    print("정답입니다.")
else :
    print("정답이 아닙니다.")