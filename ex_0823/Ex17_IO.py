# 파일 복사
inFile, OutFile = None, None
inFile = open("c:/temp/data.txt", "r", encoding="utf-8")  # 원본 파일 경로
OutFile = open("c:/temp/data3.txt", "w", encoding="utf-8")  # 복사할 파일 경로

inList = inFile.readlines()
for str in inList:  # 0부터 list의 끝까지
    OutFile.writelines(str)
inFile.close()
OutFile.close()
