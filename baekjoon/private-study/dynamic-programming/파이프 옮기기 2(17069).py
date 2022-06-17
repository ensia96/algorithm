N = range(int(input()))
A = [[*map(int, input()[::2])]for i in N]
D = [[3*[0]for j in N]for i in N]
D[0][1][2] = 1-(A[0][1] | A[0][0])
for i in N:
    for j in N:
        if A[i][j] or (i, j) == (0, 1):
            continue
        D[i][j] = (sum(D[i-1][j][:2])*(i > 0), sum(D[i-1][j-1])*(i*j > 0)
                   * (A[i-1][j]+A[i][j-1] < 1), sum(D[i][j-1][1:])*(j > 0))
print(sum(D[-1][-1]))
