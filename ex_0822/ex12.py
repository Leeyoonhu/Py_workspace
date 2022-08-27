# 튜플(tuple) => 값 수정x, 읽기 전용, 리스트와 다르게 []없음
numbers = (10, 20, 30)
print(type(numbers))

# 튜플 => 리스트 전환
numbers = (1, 2, 3)
data = list(numbers)
print(data)

# 리스트 => 튜플 전환
data = tuple(data)
print(data)

# 튜플 자체는 슬라이스 해서 읽기 가능
numbers = (10, 20, 30, 40)
print(numbers[0] + numbers[2])
print(numbers[1:3])
print(numbers[1:])
print(numbers[-3:])

# 튜플끼리 연산 가능
numbers = (10, 20, 30, 40)
letters = ("a", "b")
print(numbers + letters)  # 둘 다 튜플형이기때문에 연산 가능
print(letters * 3)

# 항목이 하나인 경우 구분자 ,를 써줘야만 튜플로 인식 가능
numbers = 10
print(type(numbers))  # 정수형

numbers = (10,)
print(type(numbers))  # 튜플형

numbers = (10, 20)
# 튜플형은 값 수정 불가, []의 유무로 리스트와 구분가능
numbers.append(40)
numbers[0] = 30
del numbers[0]

# 단, 튜플 자체는 삭제 가능
del numbers
print(numbers)
