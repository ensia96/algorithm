n = int(input())
N = range(n)
M = 8**8
A = 0
D = [[*map(int, input().split())]for _ in N]
for k in N:
    for i in N:
        for j in N:
            D[i][j] > D[i][k]+D[k][j] and exit(print(-1))
for k in N:
    D[k][k] = M
    for i in N:
        for j in N:
            if D[i][j] == D[i][k]+D[k][j]:
                D[i][j] = M
print(sum(D[i][j]for i in N for j in N if D[i][j] != M)//2)
