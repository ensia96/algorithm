n, m = map(int, input().split())
n += 1
D = [{} for i in ' '*n]
for _ in ' '*(n-2):
    u, v, d = map(int, input().split())
    D[u][v] = D[v][u] = d


def F(i, d):
    if i == b:
        print(d)
        return
    v[i] = 1
    for j in D[i]:
        if not v[j]:
            F(j, D[i][j]+d)


for _ in ' '*m:
    a, b = map(int, input().split())
    v = [0]*n
    F(a, 0)
