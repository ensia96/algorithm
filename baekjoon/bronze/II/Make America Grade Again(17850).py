W, *w = open(0)
d = [0] * 8
for l in w:
    i = 'LHPE'.find(l[0])
    x, y = map(int, l.split()[2].split('/'))
    d[i] += x
    d[i + 4] += y
print(int(sum(int(W.split()[i]) * d[i] / d[i + 4]for i in range(4))))
