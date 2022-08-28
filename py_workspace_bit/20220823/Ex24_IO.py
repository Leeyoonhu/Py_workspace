import os
from sqlite3 import Timestamp

if not os.path.isdir("c:/log"):
    os.mkdir("c:/log")

if not os.path.exists("c:/log/mylog.txt"):  # 해당 경로에 파일이 없으면
    outFile = open("c:/log/mylog.txt", "w", encoding="utf-8")  # 생성
    outFile.write("기록 시작\n")  # 파일 생성 후 기록시작만 적어주고 닫음
    outFile.close()

with open("c:/log/mylog.txt", "a", encoding="utf-8") as outFile:  # 파일에 이어쓰기
    import random, datetime  # datetime => 시간 관련 모듈

    for i in range(1, 11):
        timestamp = str(datetime.datetime.now())  # now() => 컴퓨터의 현재 시각을 객체로 만들어 반환
        # 현재 시간정보가 적힌 str형 timestamp

        num = random.randint(1, 100)  # 1~ 100난수가 적힌 num
        log_line = timestamp + "\t" + str(num) + "생성" + "\n"  # log line 10개 생성
        outFile.write(log_line)
