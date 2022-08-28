# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력
str = input()
if str.islower():
    print(str.upper())
else:
    print(str.lower())
