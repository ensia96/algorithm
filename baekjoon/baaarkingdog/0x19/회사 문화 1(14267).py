import sys
L, n = lambda: map(int, sys.stdin.readline().split()), 0
n, m = L()
P, C, A = [*L()], [[]for _ in ' '*(n+1)], [0]*n
for i in range(1, n):
    C[P[i]] += [i+1]
for _ in ' '*m:
    i, w = L()
    q = [i]
    for p in q:
        A[p-1] += w
        for c in C[p]:
            q += [c]
print(*A)
