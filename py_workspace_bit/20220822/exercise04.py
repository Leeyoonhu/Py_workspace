# 로그인 프로그램
# ID - PWD 를 각각 key-value 쌍으로 딕셔너리에 저장
dic1 = {"conan": 1111, "rose": 2222, "ran": 3333}

# 프로그램이 실행되면 사용자가 입력한 아이디와 패스워드를 입력
# 등록된 아이디와 패스워드가 같아야만 로그인 성공
ID = input("사용자의 아이디 입력 : ")
PWD = input("사용자의 패스워드 입력 : ")
if ID in dic1.keys():
    if int(PWD) == dic1[ID]:
        print("로그인에 성공하셨습니다.")
    else:
        print("비밀번호가 틀렸습니다")
else:
    print("등록된 사용자가 아닙니다. 회원 정보를 확인하세요")
