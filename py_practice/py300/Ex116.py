# 입력받은 시간이 정각인지 판별
min  = (input(">> 현재시간:"))
if min[3:] == "00":
    print("정각입니다")
else :
    print("정각이 아닙니다.")