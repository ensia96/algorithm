n, m = map(int, input().split())
E = [[]for _ in ' '*-~n]
for _ in ' '*m:
    a, b, c = map(int, input().split())
    E[a] += (b, c),
    E[b] += (a, c),
a, b = map(int, input().split())
A = 0
l, r = 0, 10**9
while l <= r:
    m, Q, V = (l+r)//2, [a], [1]*-~n
    V[a] = 0
    for x in Q:
        for i, j in E[x]:
            if V[i] and j >= m:
                V[i] = 0
                Q += i,
    if V[b]:
        r = m-1
    else:
        l, A = m+1, m
print(A)
