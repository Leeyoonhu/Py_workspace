# https://wikidocs.net/7025

price = ["20180728", 100, 130, 140, 150, 160, 170]
# 날짜 정보 제외 출력
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 홀수만 출력
print(nums[::2])

# 짝수만 출력
print(nums[1::2])

nums = [1, 2, 3, 4, 5]
# 슬라이싱으로 역순 출력
print(nums[::-1])

interest = ["삼성전자", "LG전자", "Naver"]
# 삼성전자와 Naver만 출력
print("%s %s" % (interest[0], interest[2]))

interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
# 모든 속성 출력
print(interest[0], interest[1], interest[2], interest[3], interest[4])

# 각 속성사이에 구분자 / 추가
print("/".join(interest))  # "구분자".join(리스트명)

# 각 속성 사이에 줄바꿈
print("\n".join(interest))

string = "삼성전자/LG전자/Naver"
# /구분자로 나누어 3단어를 interest에 넣고 출력
interest = string.split("/")
print(interest)

data = [2, 4, 3, 1, 5, 10, 9]
# 오름차순 정렬
data.sort()
print(data)
