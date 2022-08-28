# Set 사용하여 Set만들기
a = set("apple")  # Set은 중복값 1번만
print(a)

b = set(range(5))  # 0부터 5까지
print(b)

c = set()  # 공집합 표현
print(c)

# 딕셔너리와 셋은 {}를 사용하는데, 기본적으로는 딕셔너리가 우선
c = {}  # 기본 타입이 딕셔너리이므로 공집합 표현 불가능
print(type(c))

c = set()  # 따라서 공집합 표현 시 Set을 이용
print(type(c))
