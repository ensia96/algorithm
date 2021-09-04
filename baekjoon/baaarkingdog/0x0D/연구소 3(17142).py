l, g, a = lambda: map(int, input().split()), range, 10**5
n, m = l()
b = [[*l()]for _ in g(n)]


def t(i, d, l):
    global a
    if d == m:
        q, v = l[:], [[b[y][x]for x in g(n)]for y in g(n)]
        for y, x in q:
            for r, c in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 <= r < n and 0 <= c < n and v[r][c] in [0, 2]:
                    v[r][c] = v[y][x]+1
                    q += [(r, c)]
        a = [a, min(a, max([v[c//n][c % n]for c in g(n*n)
                    if not b[c//n][c % n]]+[3])-3)][bool(min(map(min, v)))]
        return
    for c in g(i, n*n):
        y, x = c//n, c % n
        if b[y][x] == 2:
            b[y][x] = 3
            t(c, d+1, l+[(y, x)])
            b[y][x] = 2


t(0, 0, [])
print([a, -1][a == 10**5])
