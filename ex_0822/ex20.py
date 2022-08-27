# 반복문 for loop
# for i in range(횟수): 실행문 // 횟수가 10일경우, 0~9까지 10개의 숫자 i개만큼 반복
for i in range(10):
    print("Hello World %d" % i)

# for i in range(시작, 끝): 실행문 // 시작~끝까지
for i in range(1, 3):
    print("루프 %d" % i)

# for i in range(시작, 끝, 증감): 실행문 // 시작~끝까지 증감만큼 증/감
for i in range(0, 10, 3):
    print("증가식 %d" % i)

for i in range(10, 7, -1):
    print("감소식 %d" % i)

# for i in reversed(range()): 실행문 // range()안에는 위의 조건들 올 수 있고, 역순진행
for i in reversed(range(0, 3, 1)):
    print("리버스 %d" % i)

for i in reversed(range(4, 10)):
    print("리버스다 %d" % i)
