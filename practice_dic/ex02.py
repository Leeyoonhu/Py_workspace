# https://wikidocs.net/78563
# 아이스크림 이름 key, (가격, 재고)리스트를 value, 딕셔너리 이름은 inventory
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory)

# inventory 에서 메로나의 가격 출력
print(inventory["메로나"][0], "원")

# inventory 에서 메로나의 재고 출력
print(inventory["메로나"][1], "개")

# inventory 에 데이터(월드콘) 추가
inventory["월드콘"] = [500, 7]
print(inventory)

# icecream의 key값으로만 구성된 리스트 생성
icecream = {"탱크보이": 1200, "폴라포": 1200, "빵빠레": 1800, "월드콘": 1500, "메로나": 1000}
ice = list(icecream.keys())
print(ice)

# icecream의 key값으로만 구성된 리스트 생성
ice = list(icecream.values())
print(ice)

# icecream 가격의 총합
print(sum(ice))

# icecream 딕셔너리에 new product 추가하기
