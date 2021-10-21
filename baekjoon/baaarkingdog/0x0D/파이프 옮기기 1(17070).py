n, r, a, z = int(input()), range, ((0, 1), (1, 0), (1, 1)), 0
m, g = [[*map(int, input().split())]for _ in r(n)], (n-1, n-1)
d = (a[0:1], a[1:2], a)
if m[n-1][n-1]:
    exit(print(0))


def b(y, x, s):
    global z
    i, j = y+a[s][0], x+a[s][1]
    if ((i, j) == g):
        z += 1
        return
    for S in ((0, 2), (1, 2), (0, 1, 2))[s]:
        if all((i+h < n)*(j+w < n) and not m[i+h][j+w]for h, w in d[S]):
            b(i, j, S)


b(0, 0, 0)
print(z)
