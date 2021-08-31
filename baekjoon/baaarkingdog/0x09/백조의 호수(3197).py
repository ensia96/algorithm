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
e = [*filter(lambda x: x[2] == 'A', l)]
l = [*filter(lambda x: x[2] == 'B', l)]


def s(e, l, w, t, f):
    p, e, l, w = [e, l, w][f], [[], e, e][f], [l, [], l][f], [w, w, []][f]
    v = [[0] * c for _ in g(r)]
    for a, b, k in p:
        for x, y in [(a + 1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if 0 <= x < r and 0 <= y < c and not v[x][y]:
                u = m[x][y]
                if u in d and k in d and u != k:
                    return t
                if u == 'X':
                    if f == 0:
                        e += [(a, b, k)]
                    if f == 1:
                        l += [(a, b, k)]
                    if f == 2:
                        m[x][y] = '.'
                else:
                    w += [(x, y, '.')]
                if k in d and u == '.':
                    p += [(x, y, k)]
                    v[x][y] = 1
                    m[x][y] = k
    if f == 2:
        t += 1
    return s(e, l, w, t, (f + 1) % 3)


print(s(e, l, w, 0, 0))
