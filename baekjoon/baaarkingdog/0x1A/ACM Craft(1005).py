import sys
I = sys.stdin.readline
L, T = lambda: map(int, I().split()), int(I())


def F(x): A[x] = max(A[i] > ~0 and A[i] or F(i)
                     for i in C[x] or [0])+D[x]if C[x]else D[x]; return A[x]


for _ in ' '*T:
    n, k = L()
    A, C, D = [-1]*-~n, [0]+[[]for _ in ' '*n], [0]+[*L()]
    for _ in ' '*k:
        a, b = L()
        C[b] += a,
    print(F(int(I())))
