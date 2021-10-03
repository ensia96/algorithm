l, g = lambda: map(int, input().split()), range
r, c, t = l()
b = [[*l()]for _ in g(r)]
l = [(i, j)for i in g(r)for j in g(c)if b[i][j] < 0]
for _ in g(t):
    v = [[0]*c for _ in g(r)]
    for a in g(r*c):
        i, j = a//r, a % r
        if b[i][j] > 0:
            for y, x in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= y < r and 0 <= x < c and b[y][x] != -1:
                    v[y][x], v[i][j] = v[y][x]+b[i][j]//5, v[i][j]-b[i][j]//5
    b = [[b[i][j]+v[i][j]for j in g(c)]for i in g(r)]
    for m in g(2):
        y, x, i, f, u = *l[m], *[(0, 1), (2, -1)][m], 4
        while u:
            p, q = [(y-1, x), (y, x+1), (y+1, x), (y, x-1)][i]
            if [0 <= p <= l[m][0], l[m][0] <= p < r][m] and 0 <= q < c:
                b[y][x], b[p][q], y, x = b[p][q], 0, p, q
                continue
            i, u = i+f, u-1
        y, x = l[m]
        b[y][x], b[y][x+1] = -1, 0
print(sum(map(sum, b))+2)
