n = int(input())
d = [[0]*(n+1) for _ in range(n)]
for i in range(n):
    t, p = map(int, input().split())
    if i+t <= n:
        for j in range(i+t, n+1):
            d[i][j] = p+d[i-1][i]
print(max(map(max, d)))
