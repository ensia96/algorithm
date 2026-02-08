_, s = open(0)
print(max(s.rfind(c) - s.find('10'[c > '0'])for c in '01') // 2)
