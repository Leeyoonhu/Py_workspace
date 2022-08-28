def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def cal(n1, n2):
    numList = []
    numList.append(add(n1, n2))
    numList.append(sub(n1, n2))
    numList.append(mul(n1, n2))
    numList.append(div(n1, n2))
    print("사칙연산 결과", numList)
