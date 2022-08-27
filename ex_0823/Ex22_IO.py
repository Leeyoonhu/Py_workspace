# 파일에 내용 쓰기
with open(
    "c:/temp/mylog.txt", "a", encoding="utf-8"
) as OutFile:  # append 해서 파일에 내용 이어쓰기
    for i in range(1, 11):
        data = "%d번째 행\n" % i
        OutFile.write(data)
