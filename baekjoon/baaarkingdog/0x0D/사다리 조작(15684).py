l, g = lambda: map(int, input().split()), range
n, m, h = l()
p, r = [[0]*n for _ in g(h+1)], 4
for _ in g(m):
    a, b = l()
    p[a-1][b-1], p[a-1][b] = 1, -1


def u():
    for i in g(n):
        q = [(0, i)]
        for y, x in q:
            if y < h:
                q += [(y+1, x+p[y][x])]
        if i != x:
            return
    return 1


def s(c, v):
    global r
    if u():
        r = min(r, c)
        return
    if c == 3 or r < c:
        return
    for i in g(v, n*h):
        y, x = i//n, i % n
        if c < r and x < n-1 and not p[y][x] and not p[y][x+1]:
            p[y][x], p[y][x+1] = 1, -1
            s(c+1, i)
            p[y][x] = p[y][x+1] = 0


s(0, 0)
print([r, -1][r > 3])
