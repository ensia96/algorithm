n, m, k = map(int, input().split())
d = [[1]+[0]*m for _ in ' '*(n+1)]
for i in range(n+1):
    for j in range(m+1):
        d[i][j] = d[i-1][j]+d[i][j-1]
if d[n][m] < k:
    exit(print(-1))
s = ''
for i in range(n+m, 0, -1):
    if n > 0 and d[n-1][m] >= k:
        s, n = s+'a', n-1
    else:
        s, k, m = s+'z', k-d[n-1][m], m-1
print(s)
