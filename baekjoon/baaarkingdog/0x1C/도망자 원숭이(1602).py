L, M = lambda: map(int, input().split()), 8**8
n, m, q = L()
n += 1
N = range(1, n)
D = [[M]*n for _ in ' '*n]
B = [0]+[*L()]
for _ in ' '*m:
    a, b, d = L()
    D[a][b] = D[b][a] = d+max(B[a], B[b])
P = [i for _, i in sorted((j, i)for i, j in enumerate(B))]
for k in N:
    t = P[k]
    for i in N:
        for j in N:
            a, b = max(B[i], B[t]), max(B[t], B[j])
            D[i][j] = min(D[i][j], D[i][t]+D[t][j]-a-b+max(a, b))
for _ in ' '*q:
    s, e = L()
    t = D[s][e]
    print(t if t < M else -1)
