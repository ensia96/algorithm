n = int(input())
L = [*map(int, input().split())]
R = [*map(int, input().split())]
D = [[0]*-~n for _ in ' '*-~n]
for i in range(n):
    for j in range(n):
        D[i+1][j+1] = max(D[i][j], (L[i] > R[j])*(D[i+1][j]+R[j]))
print(D[n][n])
