# 상품 구입 개수 1 => 5% / 2 => 10% / 3 => 20% / 4 이상 30%


def showInfo():
    menu = 0
    totalPrice = []
    cnt = 0
    rate = 0
    while True:
        menu = int(input("상품을 구매하시겠습니까? 1.구매 2.종료 "))
        if menu == 1:
            price = int(input("구매한 상품의 금액을 입력하세요 "))
            totalPrice.append(price)
            cnt += 1
        if menu == 2:
            break
    if cnt >= 4:
        rate = 30
    if cnt == 3:
        rate = 20
    if cnt == 2:
        rate = 10
    if cnt == 1:
        rate = 5
    print("할인율 : %d %s" % (rate, "%"))
    print("총합계 : %d 원" % sum(totalPrice))
    print("지불액 : %.1f 원" % (sum(totalPrice) - (sum(totalPrice) * rate) / 100))
