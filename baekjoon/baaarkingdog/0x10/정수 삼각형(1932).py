n = int(input())
d = [[0]*n for _ in range(n)]

for i in range(n):
    v = [*map(int, input().split())]
    for j in range(i+1):
        d[i][j] = v[j] + max(d[i-1][j], d[i-1][j-1])

print(max(d[n-1]))
