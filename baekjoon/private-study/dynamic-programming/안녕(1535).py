n = int(input())
L = [*map(int, input().split())]
H = [*map(int, input().split())]
D = [[0]*100 for _ in ' '*n]
for i in range(n):
    for j in range(100):
        if j < L[i-1]:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(D[i-1][j], D[i-1][j-L[i-1]]+H[i-1])
print(D[-1][99])
