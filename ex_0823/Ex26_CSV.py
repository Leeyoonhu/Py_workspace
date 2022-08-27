# CSV에서 필요한 정보만 선택적 저장하여 파일에 쓰기

line_counter = 0  # 행의 갯수
data_header = []  # 헤더 열 리스트
customer_USA_list = []  # USA국적의 고객 정보 리스트
customer = None
with open("c:/temp/customers.csv", "r") as customer_data:
    while True:
        data = customer_data.readline()  # customers.csv 의 한행 읽은 데이터
        if data == "":
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer = data.split(",")
            if customer[10].upper() == "USA":  # 11번 열 대문자가 USA일경우
                customer_USA_list.append(customer)  # USA에 해당하는 정보만 담음
        line_counter += 1
#     print("Header : ", data_header)
#     for i in range(0, 10):
#         print("Data", i, ":", customer_USA_list)
#     print(len(customer_USA_list))

with open("c:/temp/customers_USA.csv", "w") as customer_USA:  # 파일 경로 지정
    for customer in customer_USA_list:
        customer_USA.write(",".join(customer) + "\n")  # 다시 단어 사이에 구분자넣어주고 줄바꿈 넣은채로 저장
