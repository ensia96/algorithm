import collections as c
l, r = lambda: map(int, input().split()), range
n, k = l()
t, j, g, m = [[*l()]for _ in r(n)], {*r(n)}, c.deque([*l()]), c.deque([*l()])
w, d = [0]*3, [set(), g, m]


def e(a, b, c):
    if (len(d[0]) == n)+(max(w) == k):
        if w[0]-k:
            return
        exit(print(1))
    for p in [d[a][0]-1]if a else j-d[a]:
        x, y, z = [(b, c, a), (a, c, b)][t[p][d[b][0]-1] == 2]
        d[b].rotate(-1) or (d[a].rotate(-1)if a else d[a].add(p))
        w[x] += 1
        e(*sorted([x, y]), z)
        d[b].rotate() or (d[a].rotate()if a else d[a].remove(p))
        w[x] -= 1


e(0, 1, 2)
print(0)
