# 파일 내의 글자 통계 정보 출력
with open("c:/temp/data.txt", "r", encoding="utf-8") as inFile:
    contents = inFile.read()
    word_list = contents.split()  # 가져온 파일 정보를 글자 단위로 쪼갬
    line_list = contents.split("\n")  # 가져온 파일 정보를 줄바꿈 단위로 쪼갬
    print("파일의 총 길이 : ", len(contents))
    print("파일의 단어 수 : ", len(word_list))
    print("파일의 줄바꿈 수 : ", len(line_list))
