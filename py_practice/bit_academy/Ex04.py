# 땡땡마트는 오늘의 할인을 할 예정
# 할인율을 입력하면 할인가가 출력되는 프로그램 작성
priceList = {
    "쌀": 9900,
    "상추": 1900,
    "고추": 2900,
    "마늘": 8900,
    "통닭": 5600,
    "햄": 6900,
    "치즈": 3900,
}
keyList = list(priceList.keys())
discountPrice = []


def getDiscountPrice(rate):
    for i in range(len(priceList)):
        discountPrice.append(priceList[keyList[i]] * ((100 - rate) / 100))
    return discountPrice


def printPrice(priceList):
    for i in range(len(priceList)):
        print(
            "%s : %d 원 %d %s -> %d 원"
            % (keyList[i], priceList[keyList[i]], rate, "%DC", discountPrice[i])
        )


print("======================================")
print("-- 땡땡 마트 오늘의 할인 가격표 출력 --")
print("======================================")
rate = int(input("오늘의 할인율을 입력하세요. >> "))
getDiscountPrice(rate)
printPrice(priceList)
print("======================================")
