# 매개변수에 기본값(초기값) 설정
def para_function(num1, num2, num3=0):
    result = 0
    result = num1 + num2 + num3
    return result


sum = 0
sum = para_function(10, 20)  # 기본값 지정한 매개변수에 값을 넣어주지 않아도 함수 사용 가능
print("매개변수 2개만 받은 sum 의 값 : %d" % sum)
sum = para_function(10, 20, 30)  # 3번째 매개변수에 30을 넣어줬으므로 함수내의 num3 = 30
print("매개변수 3개만 받은 sum 의 값 : %d" % sum)

print()

# 단, 매개변수 중 초기값(기본값, 디폴트값)이 있는 매개변수는 없는 매개변수보다 후열에 배치해야만함
# def print_into(name, address ="비밀", age):    ==> 오류 Non-default argument ..
#     print("이름 : ", name)    ==> 기본값이 없는 매개변수(argument, parameter)는
#     print("나이 : ", age)     ==> 기본값이 있는 매개변수보다 뒤에 올수 없음
#     print("주소 ; ", address)
