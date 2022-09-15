I, R, L = input, range(4), len
w = int(I())
M = 8*w+1
C, N = [0]*M, [26*[-1]for _ in range(M)]
f, U, S = lambda x: ord(x)-65, 1, [0, 0, 0, 1, 1, 2, 3, 5, 11]
for _ in range(-~w):
    c = 0
    for s in I():
        t = f(s)
        if N[c][t] == -1:
            U = N[c][t] = U+1
        c = N[c][t]
    C[c] = 1


def F(i, j, k, l):
    if C[l]:
        A[L(k)] = A.get(L(k), set()) | {k}
    for x, y in [(i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]:
        if 0 <= x < 4 > y >= 0 and N[l][f(B[x][y])] > 0 and V[x][y]:
            V[x][y] = 0
            F(x, y, k+B[x][y], N[l][f(B[x][y])])
            V[x][y] = 1


b = int(I())
while b:
    A, B = {}, [I()for _ in ' '*4]
    for i in R:
        for j in R:
            if N[0][f(B[i][j])] != -1:
                V = [4*[1]for _ in R]
                F(i, j, '', 0)
    print(sum(S[a]*L(A[a])
          for a in A), sorted(A[max(A)])[0], sum(L(A[a])for a in A)-1)
    b -= 1
    b and I()
