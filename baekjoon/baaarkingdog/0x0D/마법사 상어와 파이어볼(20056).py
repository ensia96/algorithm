l, r = lambda: map(int, input().split()), range
n, m, k = l()
p = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
f = [(r-1, c-1, *d)for _ in r(m)for r, c, *d in [l()]]
for _ in r(k):
    b, q = [[[] for _ in r(n)]for _ in r(n)], []
    for y, x, w, s, d in f:
        b[(y+p[d][0]*s) % n][(x+p[d][1]*s) % n] += [(w, s, d)]
    for a in r(n*n):
        i, j, x, y, z = a//n, a % n, 0, 0, []
        l = len(b[i][j])
        if l < 2:
            q += [(i, j, *b[i][j][0])]if b[i][j]else[]
            continue
        for w, s, d in b[i][j]:
            x, y, z = x+w, s+y, z+[d & 1]
        if x//5:
            f = len(set(z)) > 1
            q += [(i, j, x//5, y//l, d*2+f) for d in r(4)]
    f = q
print(sum(r[2]for r in f))
