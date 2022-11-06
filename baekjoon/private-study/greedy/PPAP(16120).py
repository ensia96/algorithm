s, p = [], [*'PPAP']
for a in input():
    s += a,
    if s[-4:] == p:
        s.pop()
        s.pop()
        s.pop()
print('PPAP'if s in [['P'], p]else'NP')
