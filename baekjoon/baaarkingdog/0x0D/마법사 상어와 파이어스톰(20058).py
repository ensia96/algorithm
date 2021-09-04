l, r = lambda: map(int, input().split()), range
o, n, _ = lambda y, x: [(y+1, x), (y-1, x), (y, x+1), (y, x-1)], *l()
z, p = lambda i, j: (0 <= i < p)*(0 <= j < p), 2**n
b, s = [[*l()]for _ in r(p)], [*l()]
for a in s:
    m, q = [[0]*p for _ in r(p)], 2**a
    for y, x in [(i, j)for i in r(0, p, q)for j in r(0, p, q)]:
        for t in r(q*q):
            i, j = t//q, t % q
            m[y+i][x+j] = b[y+q-j-1][x+i]
    b, m = m, [[0]*p for _ in r(p)]
    for t in r(p*p):
        y, x = t//p, t % p
        if b[y][x]:
            m[y][x] -= sum(z(i, j) and bool(b[i][j])for i, j in o(y, x)) < 3
    b = [[b[i][j]+m[i][j]for j in r(p)]for i in r(p)]
v, m = [0]*p*p, 0
for t in r(p*p):
    y, x = t//p, t % p
    if (not b[y][x])*v[y*p+x]:
        continue
    q, c = [(y, x)], 0
    for y, x in q:
        for i, j in o(y, x):
            if z(i, j) and b[i][j] * (not v[i*p+j]):
                v[i*p+j], c = 1, c+1
                q += [(i, j)]
    m = max(m, c)
print(sum(map(sum, b)))
print(m)
