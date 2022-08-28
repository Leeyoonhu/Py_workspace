# 함수를 호출할 때, 전달하는 인자(매개변수)의 개수가 수시로 변경되는 경우 => * 기호사용
# Java의 Overloading 개념과 비슷
# 예시) 과목수에 따른 시험점수의 총합과 평균
def printAvg(*scores):  # 매개변수에 *를 붙이면 튜플형
    print(type(scores))
    total = 0
    cnt = len(scores)  # tuple scores의 길이 (과목 수)
    for score in scores:  # tuple scores 안의 객체를 꺼낸 score 변수 ==> 향상된 for문 처럼
        total += score  # 를 total 변수에 더함
    print("총점 : " + str(total) + "점")
    print("평균 : %.1f점" % (total / cnt))


printAvg(30, 40, 50)
printAvg(95, 80, 100, 95, 70, 66)
