n = int(input())
d = [[1]*10 for _ in range(n)]
for i in range(1, n):
    for j in range(10):
        d[i][j] = sum(d[i-1][:j+1]) % 10007
print(sum(d[-1]) % 10007)
