# 할인된 가격표 출력
# 할인율을 입력하면 할인된 가격이 출력되는 프로그램 작성
# 할인값을 반환하는 getDiscountPrice(rate), 입력된 데이터값을 출력하는 printPrice(priceList) 사용할 것
priceList = {
    "쌀": 9900,
    "상추": 1900,
    "고추": 2900,
    "마늘": 8900,
    "통닭": 5600,
    "햄": 6900,
    "치즈": 3900,
}
# 할인된 가격을 지닌 새로운 dictionary
keyList = list(priceList.keys())


def getDiscountPrice(rate):
    i = 0
    dPriceList = {}
    while i != 7:
        price = priceList.get(keyList[i])
        dPrice = price - ((price * rate) / 100)
        dPriceList[keyList[i]] = dPrice
        i += 1
    return dPriceList


def printPrice(priceList):
    dPriceList = getDiscountPrice(rate)
    for i in range(len(keyList)):
        print(
            "%s : %d 원 %d%s ==> %d 원"
            % (
                keyList[i],
                priceList.get(keyList[i]),
                rate,
                "% DC",
                dPriceList.get(keyList[i]),
            )
        )


# 출력문 서식
print("========================================")
print("-- 땡땡 마트 오늘의 할인 가격표 출력 --")
print("========================================")
rate = int((input("오늘의 할인율을 입력하세요. >> ")))
printPrice(priceList)
print("========================================")
