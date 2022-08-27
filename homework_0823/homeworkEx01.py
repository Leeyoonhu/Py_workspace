# radio_applier.csv
# 49회차만 뽑아서 따로 저장
line_counter = 0
header_list = []
customer_49_list = []
customer = None
with open("c:/temp/radio_applier.csv", "r") as customer_data:
    while True:
        data = customer_data.readline()
        if data == "":
            break
        if line_counter == 0:
            header_list.append(data.split(","))
        else:
            customer = data.split(",")
            if "46" in customer[2]:
                customer_49_list.append(customer)
        line_counter += 1

with open("c:/temp/daejeon_qualifier.csv", "w") as customer_49:
    for customer in customer_49_list:
        customer_49.write(",".join(customer) + "\n")
