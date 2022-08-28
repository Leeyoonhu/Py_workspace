saveLines = []

with open("c:/hello/ntmy.txt", "r", encoding="utf-8") as inFile:
    while True:
        line = inFile.readline()
        if line == "":
            break
        saveLines.append(line)

with open("c:/hello/ntmy2.txt", "w", encoding="utf-8") as outFile:
    for i in range(len(saveLines)):
        outFile.write(saveLines[i])
