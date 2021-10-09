import collections as c
l, r = lambda: map(int, input().split()), range
n, m, t = l()
b, c = [c.deque([*l()])for _ in r(n)], n*m
for _ in r(t):
    x, d, k, f = *l(), 0
    _ = [b[i-1].rotate([k, -k][d])for i in r(x, n+1, x)]
    for p in r(n*m):
        i, j = p//m, p % m
        if not b[i][j]:
            continue
        q, v = [(i, j)], b[i][j]
        for y, x in q:
            for h, w in [(y+1, x % m), (y-1, x % m), (y, (x+1) % m), (y, (x-1) % m)]:
                if (0 <= h < n) and b[h][w] == v:
                    b[h][w], f, c = 0, 1, c-1
                    q += [(h, w)]
    if f:
        continue
    a = sum(map(sum, b))/c
    for p in r(n*m):
        u = b[p//m][p % m]
        b[p//m][p % m] += (-(a < u)+(a > u))*bool(u)
print(sum(map(sum, b)))
