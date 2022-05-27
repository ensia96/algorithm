n = int(input())
L = [0]+[*map(int, input().split())]
J = [0]+[*map(int, input().split())]
D = [[0]*101 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, 101):
        if L[i] <= j:
            D[i][j] = max(D[i-1][j], D[i-1][j-L[i]] + J[i])
        else:
            D[i][j] = D[i-1][j]
print(D[n][99])
