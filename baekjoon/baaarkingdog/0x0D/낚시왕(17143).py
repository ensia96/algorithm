l, g = lambda: map(int, input().split()), range
r, c, m = l()
a, b = 0, [[0]*c for _ in g(r)]
for _ in g(m):
    y, x, s, d, z = l()
    b[y-1][x-1] = (z, s, d)
for x in g(c):
    for y in g(r):
        if b[y][x]:
            a, b[y][x] = a + b[y][x][0], 0
            break
    t = []
    for i, j in [(l//c, l % c)for l in g(r*c)if b[l//c][l % c]]:
        z, s, d = b[i][j]
        b[i][j], m = 0, s
        while m:
            ny, nx = [0, (i-1, j), (i+1, j), (i, j+1), (i, j-1)][d]
            ny, d = [(ny, d), [[(ny, d), (1, 2)][(d % 2)*(ny < 0)],
                               (r-2, 1)][(not d % 2)*(ny == r)]][d < 3]
            nx, d = [[[(nx, d), (c-2, 4)][(d % 2)*(nx == c)], (1, 3)]
                     [(not d % 2)*(nx < 0)], (nx, d)][d < 3]
            i, j, m = ny, nx, m-1
        t += [(i, j, z, s, d)]
    for i, j, z, s, d in t:
        b[i][j] = max(b[i][j], (z, s, d))if b[i][j]else(z, s, d)
print(a)
