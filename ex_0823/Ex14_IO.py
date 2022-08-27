inFile = None
inStr = ""

inFile = open("c:/temp/data.txt", "r", encoding="utf-8")
inList = inFile.readlines()  # 파일의 내용 전부를 리스트에 저장

print(inList)
inFile.close()
