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
        b[i][j] = 0
        if d < 3:
            e, l = [s-r+1+i, s-i][d == 1], r-1
            d = [[1, 2][d == 1], d][e < 0 or e//l % 2]
            i = [[e % l, l-(e % l)][d == 1], [i+s, i-s][d == 1]][e < 0]
        else:
            e, l = [s-c+1+j, s-j][d == 4], c-1
            d = [[3, 4][d == 3], d][e < 0 or e//l % 2]
            j = [[e % l, l-(e % l)][d == 4], [j+s, j-s][d == 4]][e < 0]
        t += [(i, j, z, s, d)]
    for i, j, z, s, d in t:
        b[i][j] = max(b[i][j], (z, s, d))if b[i][j]else(z, s, d)
print(a)
