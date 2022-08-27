lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

# lang1 lang2 모두 가지고있는 langs 리스트 만들기
langs = lang1 + lang2
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7]
# nums 의 최대 최소 뽑기
print("MAX : %d" % max(nums))
print("MIN : %d" % min(nums))

nums = [1, 2, 3, 4, 5]
# nums 리스트 요소의 합
print("SUM : %d" % sum(nums))

# 리스트에 저장된 데이터 갯수 출력
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print("데이터 갯수 : %d" % len(cook))  # .count(값) => 리스트 안의 특정 값 갯수 구하기

# nums 리스트의 평균 구하기
nums = [1, 2, 3, 4, 5]
print("nums의 평균 : %.1f" % (sum(nums) / len(nums)))
