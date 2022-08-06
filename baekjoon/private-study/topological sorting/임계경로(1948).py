n, m = int(input()), int(input())
E, R = [[]for _ in ' '*-~n], [[]for _ in ' '*-~n]
I, C, V = [0]*-~n, [0]*-~n, [0]*-~n
for _ in ' '*m:
    a, b, c = map(int, input().split())
    E[a] += (b, c),
    R[b] += (a, c),
    I[b] += 1
s, e = map(int, input().split())
Q = [s]
while Q:
    x = Q.pop()
    for a, b in E[x]:
        C[a] = max(C[a], C[x]+b)
        I[a] -= 1
        if not I[a]:
            Q += a,
Q, D = [e], 0
while Q:
    x = Q.pop()
    for a, b in R[x]:
        if C[x]-C[a] == b:
            if not V[a]:
                V[a] = 1
                Q += a,
            D += 1
print(C[e])
print(D)
