# license.applier.csv에서 과목에 의학총론이 포함된 리스트만 저장
line = ""
headerList = []
dataList = []
doctorList = []
cnt = 0
with open("c:/temp/license.applier.csv", "r") as inFile:
    while True:
        line = inFile.readline()
        if line == "":
            break
        if cnt == 0:
            headerList.append(line)
            cnt += 1
        else:
            dataList = line.split(",")
            if "의학총론" in dataList[4]:
                doctorList.append(line)

with open("c:/temp/license.doctor.csv", "w") as outFile:
    for i in range(len(doctorList)):
        outFile.write(doctorList[i])
