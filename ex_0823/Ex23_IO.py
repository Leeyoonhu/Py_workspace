# 디렉토리(파일) 만들기
import os

# mkdic() => 디렉토리 생성함수, 이미 있는 디렉토리는 생성 불가
if not os.path.isdir("c:/log"):  # 해당 경로에 디렉토리가 없을때만 생성하게 조건 생성
    os.mkdir("c:/log")
