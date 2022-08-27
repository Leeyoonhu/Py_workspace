# 할인된 가격표 출력
# 할인율을 입력하면 할인된 가격이 출력되는 프로그램 작성
# 할인값을 반환하는 getDiscountPrice(), 입력된 데이터값을 출력하는 printPrice() 사용할 것
# 쌀 = 9900, 상추 = 1900, 고추 = 2900, 마늘 = 8900, 통닭 = 5600, 햄 = 6900, 치즈= 3900

# 출력문 예시
# print("========================================")
# print("-- 땡땡 마트 오늘의 할인 가격표 출력 --")
# print("========================================")
# rate = int((input("오늘의 할인율을 입력하세요. >> ")))
# 출력 내용
# print("========================================")


priceList = {
    "쌀": 9900,
    "상추": 1900,
    "고추": 2900,
    "마늘": 8900,
    "통닭": 5600,
    "햄": 6900,
    "치즈": 3900,
}
keyList = list(priceList.keys())  # 키 배열 keyList


def getDiscountPrice(rate):  # 매개변수가 고정일때 값이 달라진다면, 값을 여러개 내보내는 무언가가있다
    discountPriceList = {}
    i = 0
    price = priceList.get(keyList[i])  # 키값이 '쌀'일때의 value
    while True:
        salePrice = price * ((100 - rate) / 100)  # 쌀일때의 할인가격
        discountPriceList[keyList[i]] = int(salePrice)  # 키값이 쌀일때 할인가격이 저장된 딕셔너리
        i += 1
        if i >= len(keyList):
            break
        price = priceList.get(keyList[i])  # 그다음 키값
    return discountPriceList  # 할인가격과 키값이 있는 List를 반환


def printPrice(priceList):
    discountPriceList = getDiscountPrice(rate)
    for i in range(len(priceList)):
        print(
            "%s : %d 원 %d %s -->> %d원"
            % (
                keyList[i],  # keyList의 i번째 인덱스 값
                priceList.get(keyList[i]),  # priceList의 키값이 keyList[i]일때의 value값
                rate,
                "%DC",
                discountPriceList.get(
                    keyList[i]
                ),  # discountPriceList의 키값이 keyList[i] 일때의 value값
            )
        )


print("========================================")
print("-- 땡땡 마트 오늘의 할인 가격표 출력 --")
print("========================================")
rate = int((input("오늘의 할인율을 입력하세요. >> ")))
printPrice(priceList)
print("========================================")
