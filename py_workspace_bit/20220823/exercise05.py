# 프로그램을 실행하여 일기 작성을 선택하면 일기 내용을 입력받아 파일로 저장
from time import strftime, localtime
import os

line = ""

if not os.path.isdir("c:/temp"):
    os.mkdir("c:/temp")

if not os.path.exists("c:/temp/diary.txt"):
    outFile = open("c:/temp/diary.txt", "w", encoding="utf-8")  # 생성
    outFile.close()  # 파일 생성 후 닫음

print("------------- 한 줄 일기 -------------")
while True:
    print("1.일기 작성 | 2.일기 보기 | 3. 종료")
    menu = int(input("메뉴를 선택하세요 >> "))
    if menu == 1:
        outFile = open("c:/temp/diary.txt", "a", encoding="utf-8")
        print("[%s]" % (strftime("%Y-%m-%d", localtime())), end=" ")
        str = input("일기를 작성하세요 >> ")
        outFile.write(str + "\n")
        outFile.close()
    if menu == 2:
        inFile = open("c:/temp/diary.txt", "r", encoding="utf-8")
        while True:
            line = inFile.readline()
            if line == "":
                break
            print(
                "[ %s ]%s" % (strftime("%Y-%m-%d %H:%M:%S", localtime()), line), end=""
            )
    if menu == 3:
        break
