I, R, L = input, range(4), len
w = int(I())
D = {}
S = [0, 0, 0, 1, 1, 2, 3, 5, 11]
for _ in range(-~w):
    T = D
    for s in I():
        T[s] = T = T.get(s, {})
    T[1] = 1


def F(i, j, k, l):
    if l.get(1):
        A[L(k)] = A.get(L(k), set()) | {k}
    for x, y in [(i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]:
        if 0 <= x < 4 > y >= 0 and l.get(B[x][y]) and V[x][y]:
            V[x][y] = 0
            F(x, y, k+B[x][y], l[B[x][y]])
            V[x][y] = 1


b = int(I())
while b:
    A, B = {}, [I()for _ in ' '*4]
    for i in R:
        for j in R:
            if D.get(B[i][j]):
                V = [4*[1]for _ in R]
                F(i, j, '', D)
    print(sum(S[a]*L(A[a])
          for a in A), sorted(A[max(A)])[0], sum(L(A[a])for a in A)-1)
    b -= 1
    b and I()
