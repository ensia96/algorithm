_, *L, _ = open(0)
x, y = map(lambda x: sum(x in l for l in L), '고문')
print(['힝구', '고무오리야 사랑해'][not (x-y) % 3])
