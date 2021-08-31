import collections as o
import sys
i, g = sys.stdin.readline, range
r, c = map(int, i().split())
m = [[*i().strip()] for _ in g(r)]
w, l, p = [], [], ['A', 'B']

for i in g(r):
    for j in g(c):
        if m[i][j] == 'L':
            u = p.pop()
            l += [(i, j, u)]
            m[i][j] = u
        if m[i][j] == '.':
            w += [(i, j, '.')]
d = 'AB'
e = o.deque([*filter(lambda x: x[2] == 'A', l)])
l = o.deque([*filter(lambda x: x[2] == 'B', l)])
w = o.deque(w)


def s(e, l, w, t, f):
    p = [e, l, w][f]
    if p == e:
        e = o.deque([])
    if p == w:
        w = o.deque([])
    if p == l:
        l = o.deque([])
    v = [[0] * c for _ in g(r)]
    while p:
        a, b, k = p.popleft()
        for x, y in [(a + 1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if 0 <= x < r and 0 <= y < c and not v[x][y]:
                u = m[x][y]
                if u in d and k in d and u != k:
                    return t
                if u == 'X':
                    if f == 0:
                        e.append((a, b, k))
                    if f == 1:
                        l.append((a, b, k))
                    if f == 2:
                        m[x][y] = '.'
                else:
                    w.append((x, y, '.'))
                if k in d and u == '.':
                    p.append((x, y, k))
                    v[x][y] = 1
                    m[x][y] = k
    if f == 2:
        t += 1
    return s(e, l, w, t, (f + 1) % 3)


print(s(e, l, w, 0, 0))
