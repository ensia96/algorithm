import sys
import itertools as t
i, g = sys.stdin.readline, range
n, m = int(i()), [[[0, 0] for _ in g(5)] for _ in g(5)]
a, c = lambda: [i().split() for _ in g(4)], t.permutations(g(n), 3)
l = [[[[int(a[i][j]), {'R': 7, 'G': 3, 'B': 5, 'Y': 2, 'W': 0}[b[i][j]]] for i in range(4)]
      for j in range(4)] for a, b in [[a(), a()]for _ in g(n)]]


def r(m): return [[m[3-j][i] for j in g(4)] for i in g(4)]
def p(m): return sum(m[i][j][0] * m[i][j][1] for i in g(5) for j in g(5))
def d(m): return [[[a, b] for a, b in l] for l in m]


def s(a, b, c, m):
    i, j, k, e = l[a], l[b], l[c], 0
    for x in g(4):
        for aa, bb in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            u = f(i, d(m), aa, bb)
            for y in g(4):
                for cc, dd in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                    v = f(j, d(u), cc, dd)
                    for z in g(4):
                        for ee, ff in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                            e = max(e, p(f(k, d(v), ee, ff)))
                        k = r(k)
                j = r(j)
        i = r(i)
    return e


def f(i, m, x, y):
    for a in g(4):
        for b in g(4):
            u, v = i[a][b]
            h = m[a+x][b+y][0]+u
            m[a+x][b+y][0] = [[h, 9][h > 9], 0][h < 0]
            if v:
                m[a+x][b+y][1] = v
    return m


print(max(s(*i, m)for i in c))
