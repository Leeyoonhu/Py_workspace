# tuple로 dictionary 만들기
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))  
print(result)