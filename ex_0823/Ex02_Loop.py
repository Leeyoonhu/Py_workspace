# break 로 반복문 탈출하기
i = 0
while True:
    print(i, end=" ")  # 반복 실행문
    i += 1  # 변화식(==증감식)
    if i == 5:  # 무한루프 빠져나갈 조건
        break
print()

for i in range(10):  # 0부터 9까지
    print(i, end=" ")  # 반복 실행문
    if i == 5:  # 반복문을 빠져나갈 조건
        break
print()

# continue 로 실행 건너뛰기
for i in range(10):  # 0부터 9까지
    if i % 2 == 0:  # 짝수일경우
        continue  # 실행 건너뜀
    print(i, end=" ")  # 홀수일경우 출력
print()

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
