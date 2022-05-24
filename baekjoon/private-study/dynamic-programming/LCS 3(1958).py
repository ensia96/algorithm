A = input()
B = input()
C = input()
a, b, c = len(A), len(B), len(C)
D = [[[0]*-~c for _ in ' '*-~b]for _ in ' '*-~a]
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            if A[i-1] == B[j-1] == C[k-1]:
                D[i][j][k] = D[i-1][j-1][k-1]+1
            else:
                D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k], D[i][j][k-1])
print(max(map(max, map(max, D))))
