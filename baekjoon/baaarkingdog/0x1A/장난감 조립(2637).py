l, A = lambda: map(int, input().split()), {}
n = int(input())
C, Q = [{}for _ in ' '*-~n], [(n, 1)]
for _ in ' '*int(input()):
    x, y, k = l()
    C[x][y] = k
for x, y in Q:
    if C[x]:
        for z in C[x]:
            Q += (z, C[x][z]*y),
    else:
        A[x] = A.get(x, 0)+y
for x in sorted(A):
    print(x, A[x])
