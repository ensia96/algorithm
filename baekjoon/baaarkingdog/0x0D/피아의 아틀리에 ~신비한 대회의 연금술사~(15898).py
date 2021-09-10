import itertools as t
import copy as c
i, g, l = input, range, []
n, m, d = int(i()), [[[0, 'W'] for _ in g(5)] for _ in g(5)], c.deepcopy
a, c = lambda: [i().split() for _ in g(4)], t.permutations(g(n), 3)
_ = [l.append([a(), a()])for _ in g(n)]
w = [(0, 0), (1, 0), (0, 1), (1, 1)]
t = {'R': 7, 'G': 3, 'B': 5, 'Y': 2, 'W': 0}
r, _ = lambda m: [[m[3-j][i] for j in g(4)] for i in g(4)], 0
p, _ = lambda m: sum(m[i][j][0] * t[m[i][j][1]] for i in g(5) for j in g(5)), 0
l = [[[[int(a[i][j]), b[i][j]] for i in range(4)]
      for j in range(4)] for a, b in l]


def s(a, b, c, m):
    i, j, k, e = l[a], l[b], l[c], 0
    for x in g(4):
        for aa, bb in w:
            u = f(i, m, aa, bb)
            for y in g(4):
                for cc, dd in w:
                    v = f(j, u, cc, dd)
                    for z in g(4):
                        for ee, ff in w:
                            e = max(e, p(f(k, v, ee, ff)))
                        k = r(k)
                j = r(j)
        i = r(i)
    return e


def f(i, k, x, y):
    m = d(k)
    for a in g(4):
        for b in g(4):
            u, v = i[a][b]
            h = m[a+x][b+y][0]+u
            m[a+x][b+y][0] = [[h, 9][h > 9], 0][h < 0]
            if v != 'W':
                m[a+x][b+y][1] = v
    return m


print(max(s(*i, m)for i in c))
