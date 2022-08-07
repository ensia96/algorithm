n, m = map(int, input().split())
E = [[]for _ in ' '*-~n]
I, A = [0]*-~n, [1]*-~n
for _ in ' '*m:
    a, b = map(int, input().split())
    E[a] += b,
    I[b] += 1
Q = [i for i in range(1, n+1)if not I[i]]
while Q:
    x = Q.pop()
    for e in E[x]:
        if I[e]:
            I[e] -= 1
            if not I[e]:
                A[e] = A[x]+1
                Q += e,
print(*A[1:])
