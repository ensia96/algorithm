i, r = input, range
n, p, d = int(i()), [*map(int, i().split())], [0]
for i in r(n):
    d += [max(d[i-j]+p[j]for j in r(i+1))]
print(d[-1])
