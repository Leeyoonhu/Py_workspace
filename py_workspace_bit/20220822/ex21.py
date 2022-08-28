# 반복문 for loop
# 객체로 반복하기
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

students = ["conan", "rose", "ran"]
for i in students:
    print(i)

for i in "Hello":
    print(i, end=" ")  # 기본 print 는 println느낌 // end=""를 주면print /
print()

for i in reversed("Hello"):
    print(i, end=" ")
print()

# 반복문으로 합 구하기
sum = 0
for i in range(1, 11):
    sum += i
print("1부터 10까지의 합 : %d" % sum)

sum = 0
for i in range(501, 1001, 2):
    sum += i
print("500부터 1000까지 홀수의 합 : %d" % sum)

sum = 0
for i in range(0, 101, 7):
    sum += i
print("0부터 100까지 7의 배수의 합 : %d" % sum)

sum = 0
num = int(input("값을 입력하세요 : "))
for i in range(1, num + 1):
    sum += i
print("1부터 %d까지의 합계 : %d" % (num, sum))
