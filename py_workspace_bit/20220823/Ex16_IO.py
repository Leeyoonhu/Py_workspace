# 한줄씩 입력받아 파일에 쓰기
# input()함수를 사용, 아무것도 입력하지 않은채 enter 누르면 파일쓰기 종료

outFile = None
outStr = ""
outFile = open("c:/temp/data2.txt", "w", encoding="utf-8")
while True:
    outStr = input("내용 입력 : ")
    if outStr == "":  # 내용이 없으면 그만
        break
    outFile.writelines(outStr + "\n")  # 내용이 있으면 계속 쓰기
outFile.close()
