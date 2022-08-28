# list 로 dictionary 만들기
data = ["09/05", "09/06", "09/07", "09/08", "09/09"]
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(data, close_price))
print(close_table)