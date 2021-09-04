n, m = map(int, input().split())
dx, dy, s, g = [1, -1, 0, 0], [0, 0, -1, 1], [], range
v = [[[[0] * m for i in g(n)] for i in g(m)] for i in g(n)]

for i in g(n):
    a = [*input()]
    s += [a]
    for j in g(m):
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j

q = [(ri, rj, bi, bj, 1)]
v[ri][rj][bi][bj] = 1


def e(i, j, x, y):
    c = 0
    while s[i + x][j + y] != "#" and s[i][j] != "O":
        i += x
        j += y
        c += 1
    return i, j, c


for ri, rj, bi, bj, d in q:
    if d > 10:
        break
    for i in g(4):
        nri, nrj, rc = e(ri, rj, dx[i], dy[i])
        nbi, nbj, bc = e(bi, bj, dx[i], dy[i])
        if s[nbi][nbj] != "O":
            if s[nri][nrj] == "O":
                exit(print(d))
            if (nri, nrj) == (nbi, nbj):
                if rc > bc:
                    nri -= dx[i]
                    nrj -= dy[i]
                else:
                    nbi -= dx[i]
                    nbj -= dy[i]
            if not v[nri][nrj][nbi][nbj]:
                v[nri][nrj][nbi][nbj] = 1
                q += [(nri, nrj, nbi, nbj, d + 1)]
print(-1)

# 풀이 참고 : https://pacific-ocean.tistory.com/346
