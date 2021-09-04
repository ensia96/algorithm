l, r = lambda: map(int, input().split()), range
n, m = l()
b, d = [[*l()] for _ in r(n)], {k+1: [] for k in r(5)}
t = [(d[b[y][x]].append(y*m+x)) for y in r(n) for x in r(m) if 0 < b[y][x] < 6]
k, e = sum(b[y][x] == 6 for y in r(n) for x in r(m)), 0
t = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for f in d:
    if d[f]:
        l = len(d[f])
        for i in r(l):
            a, u = [[] for _ in r(4)], d[f][i]
            for j in r(4):
                w = [u]
                a[j] += [u]
                for g in w:
                    y, x = g//m+t[j][0], g % m+t[j][1]
                    if 0 <= y < n and 0 <= x < m and b[y][x] == 0:
                        w += [y*m+x]
                        a[j] += [y*m+x]
            d[f][i] = a
        for i in r(l):
            h, o, s, z = d[f][i]
            d[f][i] = [d[f][i], [h+o, s+z], [h+o, o+s, s+z, z+h],
                       [h+o+s, o+s+z, s+z+h, z+h+o], [h+o+s+z]][f-1]


def c(z, q, l):
    global e
    if z > 5:
        e = max(e, len(set(l)))
        return
    if d[z]:
        p, a = len(d[z]), [4, 2, 4, 4, 1][z-1]
        b, f = p > 1, q+1 < p
        for i in r(a):
            c([z+1, [z+1, z][f]][b], [0, [0, q+1][f]][b], l+d[z][q][i])
    else:
        c(z+1, 0, l)


c(1, 0, [])
print(n*m-e-k)
