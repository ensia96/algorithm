i, d = input, {}

for _ in range(int(i())):
    n = int(i())
    d[n] = d.get(n, 0)+1

print(min((-d[k], k) for k in d)[1])
