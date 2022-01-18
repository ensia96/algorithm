n, m = map(int, input().split())
n += 1
D = [[0]*n for _ in ' '*n]
for _ in ' '*(n-2):
    u, v, d = map(int, input().split())
    D[u][v] = D[v][u] = d
for _ in ' '*m:
    a, b = map(int, input().split())
    q, v = [(a, 0)], [0]*n
    for i, d in q:
        if i == b:
            print(d)
            break
        for j in range(1, n):
            if D[i][j] and not v[j]:
                v[j] = 1
                q += [(j, D[i][j]+d)]
