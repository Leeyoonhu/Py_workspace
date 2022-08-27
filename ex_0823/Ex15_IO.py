# 파일명을 사용자 입력 받아 파일 내용 출력하기
inFile = None
inStr = ""

fileName = input("파일명을 입력하세요 : ")

inFile = open(fileName, "r", encoding="utf-8")
inList = inFile.readlines()  # 파일의 모든 행 가져오기
for inStr in inList:
    print(inStr, end="")
inFile.close()
