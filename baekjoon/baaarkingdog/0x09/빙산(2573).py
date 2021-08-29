import sys

i = sys.stdin.readline
l, r = lambda: map(int, i().split()), range
n, m = l()
b, c = [[*l()] for _ in r(n)], 0


def f():
    a, v = 0, [[0] * m for _ in r(n)]
    for i in r(1, n - 1):
        for j in r(1, m - 1):
            if a > 1:
                return a
            if b[i][j] and not v[i][j]:
                a += 1
                v[i][j] = 1
                q = [(i, j)]
                for e, f in q:
                    for x, y in [(e+1, f), (e-1, f), (e, f+1), (e, f-1)]:
                        if not v[x][y]:
                            if b[x][y]:
                                v[x][y] = 1
                                q += [(x, y)]
                            else:
                                if b[e][f] > 0:
                                    b[e][f] -= 1
    return a


while 1:
    z = f()
    if z != 1:
        print(c if z > 1 else 0)
        break
    c += 1
