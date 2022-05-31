n = int(input())
L = [*map(int, input().split())]
R = [*map(int, input().split())]
D = [[0]*-~n for _ in ' '*-~n]
for i in range(n)[::-1]:
    for j in range(n)[::-1]:
        D[i][j] = max(D[i+1][j+1], D[i+1][j], (L[i] > R[j])*(D[i][j+1]+R[j]))
print(D[0][0])
