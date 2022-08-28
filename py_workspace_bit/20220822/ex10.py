# 리스트
students = ["conan", "rose"]
students.append("ran")  # .append() 리스트에 값 추가
print(students)

students.extend(["kid", "detective"])  # .extend() 리스트에 리스트를 추가
print(students)

students.insert(0, "areum")  # .insert(index, 값) 리스트의 index번째에 값 추가
print(students)

students.remove("detective")  # .remove(값) 리스트의 해당 값 삭제
print(students)

students.pop()  # .pop() 해당 리스트(배열)의 마지막 값 꺼내기, stack의 pop처럼 FILO
print(students)

del students[0]  # . del ~ index // 해당 인덱스의 값 삭제
print(students)

students[1:2] = ["detective", "areum"]  # 1~2번 인덱스 사이[1번 인덱스 위치]에 해당 리스트 값 대체
print(students)
