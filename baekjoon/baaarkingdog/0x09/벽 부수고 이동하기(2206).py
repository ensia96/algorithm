import sys

i, r, t, p = sys.stdin.readline, range, int, map
n, m = p(t, i().split())
a, q = -1, [(0, 0, 0)]
b = [[*p(t, [*i().strip()])] for _ in r(n)]
v = [[[0, 0] for _ in r(m)] for _ in r(n)]

for i, j, f in q:
    if i == n - 1 and j == m - 1:
        a = v[i][j][f] + 1
        break
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < n and 0 <= y < m:
            if b[x][y] == 0 and v[x][y][f] == 0:
                v[x][y][f] = v[i][j][f] + 1
                q += [(x, y, f)]
            if b[x][y] == 1 and not f:
                v[x][y][1] = v[i][j][f] + 1
                q += [(x, y, 1)]

print(a)

# 풀이 참고 : https://tmdrl5779.tistory.com/15
