# CSV(Comma Separate Values) : ,를 기준으로 나누어진 csv 파일은 어디서나 사용할 수 있는 텍스트 데이터
# 첫 줄에는 테이블의 헤더(필드, 열 이름)
# 둘째 줄 이후는 인스턴스(행, 튜플)

# 파일 개체를 사용하여 데이터 다루기
line_counter = 0  # 읽은 행의 갯수
data_header = []  # 헤더 또는 열의 이름 저장
customer_list = []  # 실제 데이터 저장

with open("c:/temp/customers.csv") as customer_data:  # customer.csv 읽기
    while True:
        data = customer_data.readline()  # 한 줄을 읽어온 데이터
        if data == "":  # 더 읽을 데이터가 없을 경우
            break
        if line_counter == 0:  # 읽은 행의 갯수가 0일경우(첫줄일경우)
            data_header.append(data.split(","))  # 읽어온 한 행의 데이터를 , 구분으로 쪼갠 열의이름 저장
        else:
            customer_list.append(data.split(","))  # 그 외는 ,구분으로 쪼개서 customer_list에 저장
        line_counter += 1
    print("Header : ", data_header)  # 헤더 열의 값 표시
    for i in range(0, 10):  # 10개의 행
        print("Data", i, ":", customer_list[i])
    print(len(customer_list))  # 인스턴스(튜플, 행)의 갯수 출력
