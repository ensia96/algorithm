i, t, g = input, int, range
for _ in g(t(i())):
    n = t(i())
    d = [0, 1, 2, 4] + [0]*n
    for _ in g(4, n+1):
        d[_] = d[_-1]+d[_-2]+d[_-3]
    print(d[n])
