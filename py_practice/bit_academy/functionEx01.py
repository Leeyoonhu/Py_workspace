def printAvg(*scores):  # 매개변수에 *를 붙이면 튜플형
    print(type(scores))
    total = 0
    cnt = len(scores)  # tuple scores의 길이 (과목 수)
    for i in range(cnt):
        total += scores[i]

    for score in scores:
        total += score
    print("총점 : " + str(total) + "점")
    print("평균 : %.1f점" % (total / cnt))


printAvg(30, 40, 50)
printAvg(95, 80, 100, 95, 70, 66)
