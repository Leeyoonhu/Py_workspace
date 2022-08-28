# 반복문으로 구구단 출력
dan = 3  # 3단만 출력
# for i in range(1, 10):
#     print("%d * %d = %d" % (dan, i, dan * i))


# 2단부터 9단까지 출력
for j in range(2, 10):
    print("## %d단 ##" % j)
    for i in range(1, 10):
        print("%d * %d = %d" % (j, i, j * i))

# 2단부터 9단까지 가로로 출력
for k in range(2, 10):
    print("## %d단 ## " % k, end="  ")
print()
for j in range(1, 10):
    for i in range(2, 10):
        print("%d * %d = %2d" % (i, j, i * j), end="  ")
    print()
