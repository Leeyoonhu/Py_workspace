def sum(scoreList):
    sum = 0
    for score in scoreList:
        sum += score
    return sum


def avg(scoreList):
    cnt = len(scoreList)
    return int(sum(scoreList) / cnt)


def passOrFail(scoreList):
    count = 0
    if avg(scoreList) >= 60:
        for score in scoreList:
            if score < 40:
                count += 1
        if count == 0:
            print("pass")
        else:
            print("fail")
    else:
        print("fail")
