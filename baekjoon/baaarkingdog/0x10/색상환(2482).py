i, r = input, range
n, k = int(i()), int(i())
d, m = [[0]*(k+1)for _ in r(n+1)], 10**9+3
for i in r(n+1):
    d[i][0], d[i][1] = 1, i
for i in r(2, n+1):
    for j in r(2, k+1):
        d[i][j] = (d[i-2][j-1]+d[i-1][j]) % m
print((d[n-1][k]+d[n-3][k-1]) % m)

# 풀이 참고 : https://akim9905.tistory.com/71
