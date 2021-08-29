import sys

i = sys.stdin.readline
l, r = lambda: map(int, i().split()), range
n, m = l()
b, g = [[*l()] for _ in r(n)], lambda x: r(1, x - 1)
p, a, c = lambda: ((i, j) for j in g(m) for i in g(n)), 0, 1


def s():
    v, o = [[0] * m for _ in r(n)], 0
    for i, j in p():
        if b[i][j] and not v[i][j]:
            o += 1
            v[i][j], q = 1, [(i, j)]
            for u, w in q:
                for x, y in [(u+1, w), (u-1, w), (u, w+1), (u, w-1)]:
                    if b[x][y] and not v[x][y]:
                        v[x][y] = 1
                        q += [(x, y)]
    return o


def f():
    for i, j in p():
        if b[i][j]:
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if b[i][j] and not b[x][y]:
                    b[i][j] -= 1


while 1:
    c = s()
    if c > 1:
        break
    if not c:
        a = 0
        break
    f()
    a += 1

print(a)
