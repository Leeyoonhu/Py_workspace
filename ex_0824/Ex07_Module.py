import Calculator as cal

# as "별칭"으로 별칭을 줄 수 있음
print(cal.add(1, 2))
print(cal.sub(20, 10))
print(cal.mul(3, 5))
print(cal.div(10, 2))

# from 키워드
# module 은 필요하지 않은 기능까지 가져와야 하는 비효율적인 상황이 발생할 수 있음
# 그래서 module의 전체 기능중 일부만 import 하는것도 가능함

from Calculator import add, sub

# from 뒷절에 파일 이름이 아닌, 모듈이 오는 경우는 해당 모듈의 기능만 추려서 사용할 예정임을 알 수 있음

print(add(1, 2))
print(sub(2, 1))

# 만약, 일부만 import하지 않았는데 기능(함수, 메서드) 이름만 사용할 경우 오류
# print(mul(1, 2))

# 해당 모듈의 모든 기능(함수, 메서드)을 사용하고 싶다면 *사용
from Calculator import *

print(mul(10, 20))
