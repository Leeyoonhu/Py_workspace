# 연습문제
# 사용자가 3과목의 시험점수를 입력하면 총점, 평균, 합격여부를 판단하는 메소드 3개 만들기
# 평균 60점이상이면서 모든과목이 40점 이상이면 pass, 한과목이라도 40점 미만이면 fail
import ScoreModule

# 모듈 이름이 너무 길경우, import ScoreModule as "부르고 싶은 별칭"으로 변환가능
scoreList = []
scoreList.append(int(input("1과목 점수 : ")))
scoreList.append(int(input("2과목 점수 : ")))
scoreList.append(int(input("3과목 점수 : ")))

print("총합 : %d" % ScoreModule.sum(scoreList))
print("평균 : %d" % ScoreModule.avg(scoreList))
ScoreModule.passOrFail(scoreList)


# 사용자가 정수 2개를 입력하면, 사칙연산 결과를 리스트 타입으로 반환하는 모듈 생성
import Calculator

num1 = int(input("첫 번째 정수 >> "))
num2 = int(input("두 번째 정수 >> "))
Calculator.cal(num1, num2)
