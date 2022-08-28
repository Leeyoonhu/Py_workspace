# 연습문제 // 회원 관리 시스템


class Member:
    userId = ""
    userPwd = 0

    def __init__(self, userId, userPwd):
        self.userId = userId
        self.userPwd = userPwd


class MemberManage(Member):
    members = {}

    def addMember(self, Member):
        self.userId = Member.userId
        self.userPwd = Member.userPwd
        self.members[self.userId] = self.userPwd
        print("%s님 가입 축하드려요" % self.userId)

    def loginMember(self, userId, userPwd):
        print("// 로그인 결과 ---> ", end="")
        if userId not in idList:
            print("존재하지 않는 회원입니다.\n가입하세요!")
        if userId in idList:
            if self.members[userId] == userPwd:
                print("%s 님 로그인 성공" % userId)
            else:
                print("%s 님 비밀번호 확인하세요" % userId)

    def removeMember(self, userId, userPwd):
        if userId not in idList:
            print("존재하지 않는 회원입니다.\n가입하세요!")
        if userId in idList:
            if self.members[userId] == userPwd:
                print("%s 님이 탈퇴했음" % userId)
                del self.members[userId]
            else:
                print("%s 님 비밀번호 확인하세요" % userId)

    def printMembers(self):
        print("===== 전체회원 =====")
        for i in range(len(self.members)):
            print("ID = %s / PWD : %d" % (idList[i], int(self.members[idList[i]])))
            print("------------------------")
        self.loginMember(self, "conan", 1111)
        self.loginMember(self, "rose", 1234)
        self.loginMember(self, "kid", 0000)
        self.removeMember(self, "conan", 1111)
        idList2 = list(MemberManage.members.keys())
        print("===== 전체회원 =====")
        for i in range(len(self.members)):
            print("ID = %s / PWD : %d" % (idList2[i], int(self.members[idList2[i]])))
            print("------------------------")


MemberManage.addMember(MemberManage, Member("conan", 1111))
MemberManage.addMember(MemberManage, Member("rose", 2222))
MemberManage.addMember(MemberManage, Member("ran", 3333))
idList = list(MemberManage.members.keys())
idList2 = []

# 출력문
MemberManage.printMembers(MemberManage)
