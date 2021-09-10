n = int(input())
d = [[0]*(n+1) for _ in range(n)]

for i in range(n):
    t, p = map(int, input().split())
    for j in range(n+1):
        d[i][j] = [max(d[i-1][i] + p, d[i-1][j]), d[i-1][j]][i+t > j]
print(max(map(max, d)))
