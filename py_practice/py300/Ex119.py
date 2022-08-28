# 입력한 값이 dictionary key 값이면 정답, 아닐경우 오답
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
choice = input("제가좋아하는 계절은? :")
if choice in fruit.keys():
    print("정답")
else :
    print("오답")