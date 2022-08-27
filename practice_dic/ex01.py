# https://wikidocs.net/22000
scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# start expression을 이용하여 좌측 8개의 값을 valid_score 변수에 바인딩
*valid_score, a, b = scores
print(valid_score)

# start expression을 이용하여 우측 8개의 값을 valid_score 변수에 바인딩
_, _, *valid_score = scores
print(valid_score)

# start expression을 이용하여 가운데 8개의 값을 valid_score 변수에 바인딩
_, *valid_score, _ = scores
print(valid_score)

# temp 이름의 비어있는 dictionary 만들기
temp = {}
print(type(temp))

# 아이스크림 희망가격 dictionary 만들기
icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(icecream)

# 위의 dictionary 에 아이스크림 정보 추가
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)

# 메로나 가격출력
print("메로나 가격: %d" % icecream["메로나"])

# 메로나 가격 1300으로 수정
icecream["메로나"] = 1300
print("메로나 가격: %d" % icecream["메로나"])

# 메로나 삭제
del icecream["메로나"]
print(icecream)

# 에러 발생 원인?
# print(icecream["누가바"]) ==> 누가바 key값이 없기 때문
