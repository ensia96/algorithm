n, m = map(int, input().split())
n += 1
C, D, = [[]for _ in ' '*n], [0]*n
for _ in ' '*m:
    a, b = map(int, input().split())
    C[a] += b,
    D[b] += 1
Q, A = [i for i in range(1, n)if not D[i]], []
for p in Q:
    A += p,
    for c in C[p]:
        D[c] -= 1
        if not D[c]:
            Q += c,
print(*A)
