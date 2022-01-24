n, m = map(int, input().split())
n += 1
C, D = [[]for _ in ' '*n], [0]*n
for _ in ' '*m:
    c, *o = map(int, input().split())
    for i in range(c-1):
        C[o[i]] += o[i+1],
        D[o[i+1]] += 1
Q, A = [i for i in range(1, n)if not D[i]], []
for p in Q:
    A += p,
    for c in C[p]:
        D[c] -= 1
        if not D[c]:
            Q += c,
for i in [0] if n-1-len(A) else A:
    print(i)
