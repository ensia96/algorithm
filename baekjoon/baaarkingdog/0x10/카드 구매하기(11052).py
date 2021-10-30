i, r = input, range
n = int(i())+1
p, d = [0]+[*map(int, i().split())], [[0]*(n) for _ in r(n)]
for i in r(1, n):
    for j in r(n):
        for k in range(j//i+1):
            d[i][j] = max(d[i][j], d[i-1][j], p[i]*k+d[i-1][j-i*k])
print(d[-1][-1])
