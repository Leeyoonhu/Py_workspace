# 반환값이 여러개인경우 ==> list, dictionary .. etc 사용
def multi(v1, v2):
    rList = []
    r1 = v1 + v2
    r2 = v1 - v2
    rList.append(r1)
    rList.append(r2)
    return rList  # 진짜 중요함 반환값으로 list, dictionary도 된다


myList = []
a, b = 0, 0
myList = multi(200, 100)
a = myList[0]
b = myList[1]
print("multi()함수가 반환한 값 ==> %d, %d" % (a, b))
