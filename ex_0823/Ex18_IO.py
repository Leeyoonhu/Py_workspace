# with문과 함께 사용하기 : 자동으로 파일 객체 닫기
# with open(파일명, 파일모드) as 파일 객체: 실행문
# with를 사용하면 File을 close() 해줄 필요 없음
# 예시)
with open("c:/temp/data.txt", "r", encoding="utf-8") as inFile:
    contents = inFile.read()
    print(type(contents), contents)

# 한 줄씩 읽어 리스트형으로 반환
with open("c:/temp/data.txt", "r", encoding="utf-8") as inFile:
    content_list = inFile.readlines()
    print(type(content_list))
    print(content_list)
