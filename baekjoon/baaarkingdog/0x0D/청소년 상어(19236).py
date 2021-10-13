a, r = 0, range
m = [[0]*4 for _ in r(4)]
v = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
for i in r(4):
    d = [*map(int, input().split())]
    for j in r(4):
        m[i][j] = (d[j*2], d[j*2+1]-1)


def simulate(m, y, x, c):
    global a
    m[y][x], c, sd, f = 0, c+m[y][x][0], m[y][x][1], [0]*16
    a = max(a, c)
    for h in r(16):
        i, j = h//4, h % 4
        z = m[i][j]
        if z and z[0]:
            f[z[0]-1] = (*z, i, j)
    for h in r(len(f)):
        if not f[h]:
            continue
        n, d, i, j = f[h]
        for k in r(8):
            nd = (d+k) % 8
            ni, nj = i+v[nd][0], j+v[nd][1]
            if (0 <= ni < 4)*(0 <= nj < 4)*((ni, nj) != (y, x)):
                if m[ni][nj]:
                    f[m[ni][nj][0]-1] = (*m[ni][nj], i, j)
                m[ni][nj], m[i][j] = (n, nd), m[ni][nj]
                f[n-1] = (n, nd, ni, nj)
                break
    ny, nx = y, x
    for _ in r(3):
        ny, nx = ny+v[sd][0], nx+v[sd][1]
        if (0 <= ny < 4)*(0 <= nx < 4) and m[ny][nx]:
            simulate([[m[i][j]for j in r(4)]for i in r(4)], ny, nx, c)


simulate(m, 0, 0, 0)
print(a)
