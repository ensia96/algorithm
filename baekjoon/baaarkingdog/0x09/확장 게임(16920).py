import sys
import collections as c
i, r = sys.stdin.readline, range
l, d = lambda: map(int, i().split()), c.deque
n, m, p = l()
t, b = d([*l()]), [[*i().strip()] for _ in r(n)]
l = [[] for _ in r(p)]
c = [l[int(b[i][j]) - 1].append((int(b[i][j]) - 1, i, j))
     for i in r(n) for j in r(m) if b[i][j] in '123456789']
c, l = [len(l[i]) for i in r(p)], d(d(q) for q in l)
a = sum(w.count('.') for w in b)

while l and a:
    q, w = l.popleft(), t.popleft()
    e = w
    while w:
        v, w = d(), w - 1
        while q:
            p, i, j = q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < m and b[x][y] == '.':
                    c[p], b[x][y], a = c[p] + 1, p, a-1
                    v.append((p, x, y))
        q = v
    if q:
        l.append(q)
        t.append(e)

print(*c)
