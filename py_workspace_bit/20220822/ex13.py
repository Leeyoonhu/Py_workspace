# 딕셔너리 => 중괄호로 묶여있으며 key-value 쌍, 단 key는 중복x
dic1 = {1: "one", 2: "two", 3: "three"}
print(dic1)

dic1[4] = "four"  # dic1 에 값 추가
print(dic1)

dic1[4] = "사"  # dic1 에 중복된 값은 들어갈수 없으므로 해당 key의 value값 대체
print(dic1)

del dic1[4]  # dic[4] 4번 키의 값 삭제
print(dic1)

print(dic1[1], dic1[3])  # 각 키에 해당하는 값 출력
print(dic1.get(2))  # .get(key) 해당 키의 value 값 출력

# .keys() => 모든 키값 반환
# .values() => 모든 값 반환
# .itmes() => 튜플 형태로 key-value 반환// 리스트 함수 사용 불가

print(dic1.keys())
print(dic1.values())
print(dic1.items())
