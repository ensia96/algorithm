A = input()
B = input()
n = len(A)
m = len(B)
D = [[0]*-~m for _ in ' '*-~n]
R = ''
for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            D[i][j] = D[i-1][j-1]+1
        else:
            D[i][j] = max(D[i-1][j], D[i][j-1])
print(D[i][j])
while i > 0 and j > 0:
    if D[i][j-1] == D[i][j]:
        j -= 1
    elif D[i-1][j] == D[i][j]:
        i -= 1
    else:
        R += A[i-1]
        i, j = i-1, j-1
print(R)
