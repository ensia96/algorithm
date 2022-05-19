n, m = int(input()), 1000000000
D = [[[0]*1024 for _ in ' '*10] for _ in ' '*-~n]
for i in range(1, 10):
    D[1][i][1 << i] = 1
for i in range(2, n+1):
    for j in range(10):
        for k in range(1024):
            t = k | (1 << j)
            D[i][j][t] += (j > 0 and D[i-1][j-1][k])+(j < 9 and D[i-1][j+1][k])
print(sum(D[-1][j][1023]for j in range(10)) % m)
