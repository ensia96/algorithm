import sys
I = sys.stdin.readline
L, T = lambda: map(int, I().split()), int(I())

for _ in ' '*T:
    n, k = L()
    n += 1
    A, C, D, T, Q = [0]*n, [[]for _ in ' '*n], [0]*n, [0]+[*L()], []
    for _ in ' '*k:
        a, b = L()
        C[a] += b,
        D[b] += 1
    for i in range(1, n):
        if not D[i]:
            Q += i,
            A[i] = T[i]
    for p in Q:
        for i in C[p]:
            D[i] -= 1
            A[i] = max(A[p]+T[i], A[i])
            if not D[i]:
                Q += i,
    print(A[int(I())])
