_, H, *L = map(int, open(W := 0).read().split())
for l in zip(*[iter(L)] * 3):
    a, b, c = sorted(l)
    a > H and exit(print('impossible'))
    W += [a, b][b > H]
print(W)
