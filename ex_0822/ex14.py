# Set(집합) => 순서x, 중복x, 인덱스x, 합*교*차 집합
# Set 변수 = {값1, 값2, 값3 ...}
fruits = {"strawberry", "grape", "orange"}
print(fruits)

fruits = {"strawberry", "banana", "orange", "orange"}
print(fruits)  # 중복값 한번만, 순서 상관 없이 출력
fruits.add("hello")
print(len(fruits))
print(fruits)
# print(fruits[0])  # 인덱스 사용x
