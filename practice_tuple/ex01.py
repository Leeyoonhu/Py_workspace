# https://wikidocs.net/7027

# my_variable 이름의 비어있는 튜플
my_variable = ()
print(type(my_variable))

# "닥터 스트레인지", "스플릿", "럭키" 속성을 지닌 튜플 만들기
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(type(movie_rank))

# 숫자 1이 저장된 튜플
num = (1,)
print(type(num))

# 튜플 오류 찾기
t = (1, 2, 3)
# t[0] = "a" => 튜플은 값 수정, 삭제, 삽입 불가능(읽기 전용)

t = 1, 2, 3, 4
# t가 바인딩하는 타입?
print(type(t))

t = ("a", "b", "c")
# 변수 T가  "A", "b", "c"를 가르키도록 수정
t = (t[0].upper(), "b", "c")  # 튜플은 값 수정 불가능하기때문에 새로운 튜플을 만들어야함
print(t)

interest = ("삼성전자", "LG전자", "SK Hynix")
# 튜플을 리스트로 전환하기
data = list(interest)
print(data)

# 리스트를 튜플로 전환하기
data = tuple(data)
print(data)

temp = ("apple", "banana", "cake")
a, b, c = temp
print(a, b, c)
# 다음 코드의 예상결과는?(언팩킹)
# apple banana cake

# 1~99 정수중 짝수만 저장된 튜플 생성
numbers = tuple(range(2, 100, 2))
print(numbers)
