# icu_stat.csv에서 20대 남성만 추출하여 저장
line = ""
headerList = []
dataList = []
male20List = []
cnt = 0
with open("c:/temp/icu_stat.csv", "r") as inFile:
    while True:
        line = inFile.readline()
        if line == "":
            break
        if cnt == 0:
            headerList.append(line)
            cnt += 1
        else:
            dataList = line.split(",")
            if "남" in dataList[1] and "2" in dataList[2]:
                male20List.append(line)

with open("c:/temp/male20List.csv", "w") as outFile:
    for i in range(len(male20List)):
        outFile.write(male20List[i])
