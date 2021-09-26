_, c, d = lambda: map(int, input().split()), 0, 1
n, l, r = _()
m = [[*_()] for i in range(n)]
while d:
    v, d = [0]*n*n, []
    for i in range(n*n):
        if not v[i]:
            q, v[i] = [(i//n, i % n)], 1
            for y, x in q:
                for j, k in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                    if 0 <= j < n and 0 <= k < n and not v[j*n+k] and l <= abs(m[y][x]-m[j][k]) <= r:
                        v[j*n+k] = 1
                        q += [(j, k)]
            if len(q) > 1:
                d += [q]
    for q in d:
        v = sum(map(lambda i: m[i[0]][i[1]], q))//len(q)
        for y, x in q:
            m[y][x] = v
    c += 1
print(c-1)
