D = {}
for l in [*open(0)][1:]:
    *l, = map(int, l.split())
    d = {j: i for i, j in enumerate(sorted([*set(l)]))}
    k = *(d[i]for i in l),
    D[k] = D.get(k, 0)+1
print(sum(v*~-v//2for v in D.values()))
