n = int(input())
c = [[0]*n for _ in ' '*n]
for _ in ' '*int(input()):
    a, b = map(int, input().split())
    c[a-1][b-1] = c[b-1][a-1] = 1
q, v = [0], [1]+[0]*(n-1)
for i in q:
    for j in range(n):
        if c[i][j] and not v[j]:
            q += [j]
            v[j] = 1
print(len(q)-1)
