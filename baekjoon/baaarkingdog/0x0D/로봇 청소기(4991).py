import itertools as e
u, g = input, range


def k(p, i):
    q, v, o = [(*l[p], 0)], [0]*w*h, l[i]
    for r, c, d in q:
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if (nr, nc) == o:
                t[p][i] = t[i][p] = d+1
                return
            if 0 <= nr < h and 0 <= nc < w and not v[nr*w+nc] and b[nr][nc] != 'x':
                v[nr*w+nc] = 1
                q += [(nr, nc, d+1)]


while 1:
    w, h = map(int, u().split())
    if not w+h:
        break
    a, b, t, l = 10**9, [[*u().strip()]for _ in g(h)], 0, []
    for p in g(h*w):
        i, j = p//w, p % w
        t = [t, [0, (i, j)][b[i][j] == 'o']][not t]
        l = [l, l+[(i, j)]][b[i][j] == '*']
    l, s = [t]+l, len(l)+1
    t = [[0]*s for _ in g(s)]
    _ = [k(p, i)for p, i in ((x, y)for x in g(s)for y in g(x+1, s))]
    for p in e.permutations(g(1, s), s-1):
        l = r = f = 0
        for i in p:
            if not t[r][i]:
                f = 1
                break
            l, r = l+t[r][i], i
        a = [min(a, l), a][f]
    print([a, -1][a == 10**9])
