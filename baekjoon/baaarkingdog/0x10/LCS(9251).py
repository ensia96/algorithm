I, R = input, range
a, b = I(), I()
c, d = len(a), len(b)
D = [[0]*(d+1) for _ in R(c+1)]
for i in R(c):
    for j in R(d):
        D[i+1][j+1] = a[i] == b[j] and D[i][j]+1 or max(D[i][j+1], D[i+1][j])
print(D[c][d])
