import sys
i, g = sys.stdin.readline, range
r, c = map(int, i().split())
m = [[*i().strip()] for _ in g(r)]
l, p = [], ['A', 'B']

for i in g(r):
    for j in g(c):
        if m[i][j] == 'L':
            w = p.pop()
            l += [(i, j, w)]
            m[i][j] = w
d = 'AB'
e = [*filter(lambda x: x[2] == 'A', l)]
l = [*filter(lambda x: x[2] == 'B', l)]


def s(e, l, t, f):
    p = l if f else e
    l = [] if f else l
    e = e if f else []

    for a, b, k in p:
        for x, y in [(a + 1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if 0 <= x < r and 0 <= y < c:
                u = m[x][y]
                if u == d[not f]:
                    return (t // 2) + (t % 2)
                if u == 'X':
                    if f:
                        l += [(x, y, k)]
                    else:
                        e += [(x, y, k)]
                    m[x][y] = k
                if u == '.':
                    p += [(x, y, k)]
                    m[x][y] = k
    return s(e, l, t + 1, not f)


print(s(e, l, 0, 0))
