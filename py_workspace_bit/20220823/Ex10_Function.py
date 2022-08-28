# 인수와 매개변수의 순서 불일치
# def fun1(v1, v2) ==> 파라미터(parameter)
# fun1(1, 2) ==> 인수(인자, argument)


def printMemberInfo(name, email, major, year):
    print("name :\t", name)
    print("email :\t", email)
    print("major :\t", major)
    print("year :\t", year)
    print("===============================")


printMemberInfo("conan", "conan@aaa.com", "football", 1)
printMemberInfo(
    year=4, major="chemical", name="rose", email="rose@aaa.com"
)  # 인수에서 매개변수 순서 변경
printMemberInfo(major="sports", year=3, email="ran@ccc.com", name="ran")
