n = int(input())
d = [[0]+[1]*9]+[[0]*10 for _ in range(n-1)]
for i in range(1, n):
    for j in range(10):
        if 0 < j < 9:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
        else:
            d[i][j] = d[i-1][[8, 1][not j]]
print(sum(d[-1]) % 10**9)
