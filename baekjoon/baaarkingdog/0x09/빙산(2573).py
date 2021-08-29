import sys

i = sys.stdin.readline
l, r = lambda: map(int, i().split()), range
n, m = l()
a, b, c = 0, [[*l()] for _ in r(n)], 1


def s():
    v, o = [[0] * m for _ in r(n)], 0
    for i in r(1, n - 1):
        for j in r(1, m - 1):
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
    for i, j in [(i, j) for i in r(n) for j in r(m) if not b[i][j]]:
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < n and 0 <= y < n and b[x][y]:
                b[x][y] -= 1


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
