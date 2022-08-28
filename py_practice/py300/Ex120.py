# 입력한 값이 dictionary 의 values 에 있으면 정답, 아니면 오답
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
choice = input("제가좋아하는 과일은? :")
if choice in fruit.values():
    print("정답")
else :
    print("오답")