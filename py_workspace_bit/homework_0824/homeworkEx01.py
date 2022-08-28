# 이름 연락처 주소 저장하는 클래스
# 저장 후 재실행 시 해당 파일 있으면 불러옴, 없으면 만들고
# 실행시 저장된 파일이 있으면 파일을 열어서 해당 값들을 Contact 클래스의 변수리스트에 넣어야 됨

import os


class Contact:
    nameList = []
    phoneList = []
    addrList = []

    def __init__(self, info):
        self.nameList.append(info[0])
        self.phoneList.append(info[1])
        self.addrList.append(info[2])

    def search(self, name):
        for i in range(len(self.nameList)):
            if name == self.nameList[i]:
                print(
                    "이름 : %s | 전화번호 : %s | 주소 : %s"
                    % (self.nameList[i], self.phoneList[i], self.addrList[i])
                )

    def delete(self, name):
        i = 0
        while i < len(self.nameList):
            if name == self.nameList[i]:
                del self.nameList[i]
                del self.phoneList[i]
                del self.addrList[i]
                i = 0
            else:
                i += 1

    def showCount(self):
        print("목록에 저장된 회원 수는 %d명입니다" % len(self.nameList))

    def saveFile(self):
        with open("c:/temp/contact.txt", "w", encoding="utf-8") as OutFile:
            for i in range(len(self.nameList)):
                OutFile.write(self.nameList[i] + ",")
                OutFile.write(self.phoneList[i] + ",")
                OutFile.write(self.addrList[i] + "\n")


if os.path.exists("c:/temp/contact.txt"):
    with open("c:/temp/contact.txt", "r", encoding="utf-8") as InFile:
        line = ""
        while True:
            line = InFile.readline()
            if line == "":
                break
            contact = Contact(line.strip("\n").split(","))


while True:
    print(
        "================================================================================================="
    )
    print("1.전화번호 추가 | 2.전화번호 검색 | 3.전화번호 삭제 | 4.전화번호 목록 | 5.파일로 저장 | 6.프로그램 종료")
    print(
        "================================================================================================="
    )
    menu = int(input("메뉴를 선택하세요>> "))
    if menu == 1:
        info = input("이름, 전화번호, 주소 순서대로 입력하세요 >> ").split()
        contact = Contact(info)
    if menu == 2:
        name = input("검색할 이름을 입력하세요 >>")
        contact.search(name)
    if menu == 3:
        name = input("삭제할 이름을 입력하세요 >>")
        contact.delete(name)
    if menu == 4:
        contact.showCount()
    if menu == 5:
        contact.saveFile()
    if menu == 6:
        break
