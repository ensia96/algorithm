D, y = {'S': 0, 'B': 0, 'L': 0, 'P': 0}, 0
for l in [*open(0)][1:]:
    s, x = l.split()
    D[s[0]] += int(x)
print('YNEOS'[5 not in D.values()::2])
