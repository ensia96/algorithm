i, t, g = input, int, range
for _ in g(t(i())):
    n = t(i())
    d = [0, 1, 2, 4] + [0]*n
    for i in g(4, n+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]
    print(d[n])
