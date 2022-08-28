# 입력 (input, read)
# 출력 (output, write)

# 파일 입출력
# 읽기 => 변수명 = open("파일명", "r") // 디폴트 값 (r, w이 없으면 읽기)
# 쓰기 => 변수명 = open("파일명", "w")

# r => 읽기모드, 기본값
# w => 쓰기모드, 기존 파일 있으면 덮어씀
# a => 쓰기모드, 기존 파일이 있으면 이어서 씀
# t => 텍스트 모드, 텍스트 파일 처리, 기본값

inFile = None
inStr = ""

inFile = open("c:/temp/data.txt", "r", encoding="utf-8")

while True:
    inStr = inFile.readline()  # .readline() = 한행씩 가져옴
    print(inStr, end="")  # 줄이 바뀌는 이유는 inStr안의 행 정보 마지막에 \n이 포함되어 있기때문
    if inStr == "":
        break
inFile.close()
