A, B = open(0)
n = len(A)
m = len(B)
D = [[0]*-~m for _ in ' '*n]
for i in range(n):
    for j in range(m):
        D[i][j] = (D[i-1][j-1]+1)*(A[i] == B[j])
print(max(map(max, D)))
