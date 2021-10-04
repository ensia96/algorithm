from itertools import permutations
u, g = input, range
while 1:
    w, h = map(int, u().split())
    if not w+h:
        break
    a, b = 10**9, [[*u().strip()]for _ in g(h)]
    l = [(p//w, p % w)for p in g(h*w)if b[p//w][p % w] in 'o*']
    s = len(l)
    t = [[-1]*s for _ in g(s)]
    for p in g(s):
        for i in g(p, s):
            q, v, o = [(*l[p], -1)], [0]*w*h, l[i]
            for r, c, d in q:
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if (nr, nc) == o:
                        t[p][i] = t[i][p] = d
                    if 0 <= nr < h and 0 <= nc < w and not v[nr*w+nc] and b[nr][nc] != 'x':
                        v[nr*w+nc] = 1
                        q += [(nr, nc, d+1)]
    n = permutations(g(1, s), s-1)
    for p in n:
        l = r = 0
        for i in p:
            l, r = l+t[r][i], i
        a = min(a, l)
    print(a)
