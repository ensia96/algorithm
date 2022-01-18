n, m = map(int, input().split())
n += 1
D = [[0]*n for _ in ' '*n]
for _ in ' '*(n-2):
    u, v, d = map(int, input().split())
    D[u][v] = D[v][u] = d
for i in range(1, n):
    q, v = [(i, 0)], [0]*n
    v[i] = 1
    for j, d in q:
        for k in range(1, n):
            if not v[k] and D[j][k]:
                v[k], t = 1, D[j][k]
                D[i][k] = D[k][i] = d+t
                q += [(k, d+t)]
for _ in ' '*m:
    a, b = map(int, input().split())
    print(D[a][b])
