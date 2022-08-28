with open("c:/temp/dorian.txt", "r", encoding="utf-8") as openFile:
    while True:
        data = openFile.read()
        print(data, end=" ")
        if data == "":
            break
