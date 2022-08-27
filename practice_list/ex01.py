# https://wikidocs.net/7023
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# 베트맨 추가
movie_rank.append("베트맨")
print(movie_rank)

# 닥터 스트레인지, 스플릿 사이에 슈퍼맨 넣기
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 럭키 삭제
movie_rank.remove("럭키")
print(movie_rank)

# 스플릿, 베트맨 삭제
del movie_rank[2]
del movie_rank[2]
