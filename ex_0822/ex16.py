# 합집합(Union, |) 과 교집합(Intersection, &)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a & b)  # 파이썬에서 && => and / || => or

# 차집합(Difference, -) 과 대칭 차집합(두 합집합에서 교집합뺀것, ^)
print(a - b)
print(set.difference(a, b))

print(a ^ b)
print(set.symmetric_difference(a, b))

# 대입연산자 또는 .update() 함수
a = {1, 2, 3, 4}
a |= {5}
a.update({5})
print(a)

a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
print(a)

a.intersection_update({0, 1, 2, 3, 4})  # a = {1, 2, 3, 4}와의 교집합 a에 저장
print(a)
# .update() => 합집합, .intersection_update => 교집합
