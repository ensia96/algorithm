A = input()
B = input()
n = len(A)
m = len(B)
D = [[0]*m for _ in ' '*n]
for i in range(n):
    for j in range(m):
        if A[i] == B[j]:
            D[i][j] = D[i-1][j-1]+1
print(max(map(max, D)))
