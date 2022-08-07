n, m = map(int, input().split())
E = [[]for _ in ' '*-~n]
I, A = [0]*-~n, [1]*-~n
for _ in ' '*m:
    a, b = map(int, input().split())
    E[a] += b,
    I[b] += 1
Q = [i for i in range(1, n+1)if not I[i]]
while Q:
    q = []
    for x in Q:
        for e in E[x]:
            I[e] -= 1
            if not I[e]:
                A[e] = max(A[e], A[x]+1)
                q += e,
    Q = q
print(*A[1:])
