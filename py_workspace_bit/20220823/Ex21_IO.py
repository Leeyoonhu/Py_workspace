# 텍스트 파일 저장하기
outFile = open("c:/temp/mylog.txt", "w", encoding="utf-8")
for i in range(1, 11):
    data = "%d번째 행 \n" % i  # 1~10번째 행까지 outFile 주소에 씀
    outFile.write(data)
outFile.close()
