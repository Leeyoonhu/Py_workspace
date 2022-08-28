# 실행할 때마다 한 줄씩 읽어오기
with open("c:/temp/data.txt", "r", encoding="utf-8") as inFile:
    i = 0
    while True:
        line = inFile.readline()  # 파일에서 한줄씩 읽어옴
        if line == "":  # 한줄씩 읽어온 행의 값이 없을 때
            break
        print(str(i) + ". " + line.replace("\n", ""))
        i += 1
