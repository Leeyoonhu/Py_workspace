# 리스트 안에있으면 있다, 없으면 없다
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
choice = input("종목을 입력하세요 >> ")
if choice in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")