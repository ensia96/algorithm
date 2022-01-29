import sys
I = sys.stdin.readline
L, T = lambda: map(int, I().split()), int(I())


def F(x):
    for i in C[x]:
        if A[i] < 0:
            A[i] = F(i)
        A[x] = max(A[x], A[i])
    return A[x]+D[x]


for _ in ' '*T:
    n, k = L()
    A, C, D = [-1]*-~n, [[]for _ in ' '*-~n], [0]+[*L()]
    for _ in ' '*k:
        a, b = L()
        C[b] += a,
    print(F(int(I()))+1)
