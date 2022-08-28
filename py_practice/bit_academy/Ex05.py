# radio_applier.csv 파일에서 49회차만 선별해서 저장
from itertools import count


line = ""
dataList = []
headerList = []
lineList49 = []
with open("c:/temp/radio_applier.csv", "r") as inFile:
    cnt = 0
    while True:
        line = inFile.readline()
        if line == "":
            break
        if cnt == 0:
            headerList.append(line)
            cnt += 1
        else:
            dataList = line.split(",")
            for i in range(len(dataList)):
                if "49" in dataList[2]:
                    lineList49.append(line)


with open("c:/temp/lineList49.csv", "w") as outFile:
    for i in range(len(lineList49)):
        outFile.write(lineList49[i])
