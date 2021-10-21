n, r, a = int(input()), range, ((0, 1), (1, 0), (1, 1))
m = [[*map(int, input().split())]for _ in r(n)]
d, v = (a[0:1], a[1:2], a), [[[-1]*3 for _ in r(n)]for _ in r(n)]


def b(y, x, s):
    if (y, x) == (n-1, n-1):
        return 1
    if v[y][x][s] != -1:
        return v[y][x][s]
    v[y][x][s] = 0
    for S in ((0, 2), (1, 2), (0, 1, 2))[s]:
        if all((y+h < n)*(x+w < n) and not m[y+h][x+w]for h, w in d[S]):
            v[y][x][s] += b(y+a[S][0], x+a[S][1], S)
    return v[y][x][s]


print(b(0, 1, 0))
