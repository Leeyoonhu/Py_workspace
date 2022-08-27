# 리스트
number = [1, 2, 2, 3, 4, 5, 5, 5]
print(number.count(2))  # .count(값) => 리스트 안의 특정 값 갯수 구하기

number = [10, 20, 30, 40, 50]
print(10 in number)  # A in B, B가 가진 값중에 A가 있는지 => T or F

number.reverse()  # .reverse() => 리스트 순서 변경 <==> .reversed()는 내장 함수로, list함수가아님
print(number)

number = [23, 55, 33, 22, 44, 12, 4]
number.sort()  # .sort() => 오름차순 정렬
print(number)
