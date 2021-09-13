m = [[*map(int, input().split())] for _ in range(9)]
c, g = lambda i, j: {m[_][j] for _ in range(9)}, {*range(1, 10)}
p, f = lambda i, j: {m[i//3*3+a][j//3*3+b]
                     for a in range(3) for b in range(3)}, 0
t = [(i, j) for i in range(9) for j in range(9) if not m[i][j]]
n = len(t)


def a(u):
    if u == n:
        return 1
    i, j = t[u]
    if not m[i][j]:
        for v in g-{*m[i]}-c(i, j)-p(i, j):
            m[i][j] = v
            if a(u+1):
                return 1
            m[i][j] = 0


a(0)
for _ in m:
    print(*_)
