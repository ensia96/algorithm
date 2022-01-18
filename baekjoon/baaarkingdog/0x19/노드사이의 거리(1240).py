n, m = map(int, input().split())
n += 1
D = [[0]*n for _ in ' '*n]
for _ in ' '*(n-2):
    u, v, d = map(int, input().split())
    D[u][v] = D[v][u] = d


def F(i, d):
    if i == b:
        print(d)
        return
    for j in range(1, n):
        if D[i][j] and not v[j]:
            v[j] = 1
            F(j, D[i][j]+d)


for _ in ' '*m:
    a, b = map(int, input().split())
    v = [0]*n
    F(a, 0)
