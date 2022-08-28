import os

if not os.path.isdir("c:/hello"):
    os.mkdir("c:/hello")

if not os.path.exists("c:/hello/ntmy.txt"):
    outFile = open("c:/hello/ntmy.txt", "w", encoding="utf-8")
    outFile.close()

with open("c:/hello/ntmy.txt", "a", encoding="utf-8") as outFile:
    while True:
        str = input("출력문을 작성하세요 : ")
        if str == "":
            break
        outFile.write(str + "\n")
