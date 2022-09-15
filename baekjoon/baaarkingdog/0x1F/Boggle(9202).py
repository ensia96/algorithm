I, R, L = input, range(4), len
w = int(I())
D = {}
P = [0, 0, 0, 1, 1, 2, 3, 5, 11]
for _ in ' '*w:
    T, S = D, I()
    for s in S:
        T[s] = T = T.get(s, {})
    T[1] = S


def f(S):
    T = D
    for s in S:
        T = T.get(s)
        if not T:
            return
    return 1 in T


def F(i, j, k):
    if L(k) > 8:
        return
    if f(k) and k not in A[1]:
        A[0] += P[L(k)]
        A[1].add(k)
    V[i][j] = 0
    for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
        0 <= x < 4 > y >= 0 and V[x][y] and F(x, y, k+B[x][y])
    V[i][j] = 1


I()
b = int(I())
while b:
    A, B = [0, set()], [I()for _ in ' '*4]
    for i in R:
        for j in R:
            if D.get(B[i][j]):
                V = [4*[1]for _ in R]
                F(i, j, B[i][j])
    print(A[0], sorted(A[1], key=lambda x: -L(x))[0], len(A[1]))
    b -= 1
    b and I()
