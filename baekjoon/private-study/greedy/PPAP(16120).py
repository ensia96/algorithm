s, p = [], [*'PPAP']
for a in input():
    s += a,
    if s[-4:] == p:
        s.pop()
        s.pop()
        s.pop()
print('NP'if'A' in s else'PPAP')
