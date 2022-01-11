n = int(input())
f = [[0]*n for _ in ' '*n]
for _ in ' '*int(input()):
    a, b = map(int, input().split())
    f[a-1][b-1] = f[b-1][a-1] = 1
q, v = [(0, 0)], [1]+[0]*(n-1)
for i, d in q:
    for j in range(n):
        if f[i][j] and not v[j] and d < 2:
            q += [(j, d+1)]
            v[j] = 1
print(len(q)-1)
