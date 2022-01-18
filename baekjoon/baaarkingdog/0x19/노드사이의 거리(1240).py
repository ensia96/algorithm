n, m = map(int, input().split())
n += 1
D = [[0]*n for _ in ' '*n]
for _ in ' '*(n-2):
    u, v, d = map(int, input().split())
    D[u][v] = D[v][u] = d
for i in range(1, n):
    q, v = [i], [0]*n
    v[i] = 1
    for j in q:
        for k in range(n):
            if not v[k] and D[j][k]:
                v[k] = 1
                D[i][k] = D[k][i] = min(D[i][k] or 10001, D[i][j]+D[j][k])
                q += [k]
for _ in ' '*m:
    a, b = map(int, input().split())
    print(D[a][b])
