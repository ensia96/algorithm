import sys
i, g = sys.stdin.readline, range
r, c = map(int, i().split())
m = [[*i().strip()] for _ in g(r)]
w, l, p, d = [], [], ['A', 'B'], 'AB'

for i in g(r):
    for j in g(c):
        if m[i][j] == 'L':
            u = p.pop()
            l += [(i, j, u)]
            w += [(i, j)]
            m[i][j] = u
        if m[i][j] == '.':
            w += [(i, j)]


def f(p):
    n = []
    for a, b in p:
        for x, y in [(a + 1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if 0 <= x < r and 0 <= y < c and m[x][y] == 'X':
                m[x][y] = '.'
                n += [(x, y)]
    return n


def s(p, w, t):
    l = []
    for a, b, k in p:
        for x, y in [(a + 1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if 0 <= x < r and 0 <= y < c and m[x][y] != k:
                u = m[x][y]
                if u in d:
                    return t
                if u == '.':
                    p += [(x, y, k)]
                    m[x][y] = k
                if u == 'X':
                    l += [(a, b, k)]
    return s(l, f(w), t + 1)


print(s(l, w, 0))
