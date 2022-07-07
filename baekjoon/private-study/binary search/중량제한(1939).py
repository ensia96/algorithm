n, m = map(int, input().split())
E = [[]for _ in ' '*-~n]
for _ in ' '*m:
    a, b, c = map(int, input().split())
    E[a] += (b, c),
    E[b] += (a, c),
a, b = map(int, input().split())
S, V = [(a, 10**9)], [0]*-~n
A = V[a] = 0
while S:
    x, y = S.pop()
    if x == b:
        A = max(A, y)
        continue
    for i, j in E[x]:
        t = min(y, j)
        if V[i] < t:
            V[i] = t
            S += (i, t),
print(A)
