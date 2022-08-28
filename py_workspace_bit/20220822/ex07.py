a = input(
    "500원짜리 개수 -->",
)
b = input(
    "100원짜리 개수 -->",
)
c = input(
    "50원짜리 개수 -->",
)
d = input(
    "10원짜리 개수 -->",
)
result = (int(a) * 500) + (int(b) * 100) + (int(c) * 50) + (int(d) * 10)
print("## 동전의 합계 ==> " + str(result) + "원")
