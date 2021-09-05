import copy
i, g = input, range
n = int(i())
m = [[*map(int, i().split())] for _ in g(n)]
r, d = lambda m: [[m[n-1-j][i] for j in g(n)] for i in g(n)], copy.deepcopy


def c(m):
    a, v = d(m), [[0]*n for _ in g(n)]
    for i in g(n):
        for j in reversed(g(n-1)):
            if a[i][j]:
                u, z = a[i][j], 1
                a[i][j] = 0
                for k in g(j+1, n):
                    if a[i][k]:
                        z = 0
                        if a[i][k] == u and not v[i][k]:
                            a[i][k], v[i][k] = u*2, 1
                        else:
                            a[i][k-1] = u
                        break
                if z:
                    a[i][n-1] = u
    return a


def e(t, m):
    if t == 0:
        return max(map(max, m))
    a, b = 0, d(m)
    for z in g(4):
        a = max(a, e(t-1, c(b)))
        b = r(b)
    return a


print(e(5, m))
