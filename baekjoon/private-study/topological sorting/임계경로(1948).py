n = int(input())
m = int(input())
E = [[]for _ in ' '*-~n]
R = [[]for _ in ' '*-~n]
for _ in ' '*m:
    a, b, c = map(int, input().split())
    E[a] += (b, c),
    R[b] += (a, c),
s, e = map(int, input().split())
Q, C = [(s, 0)], [0]*-~n
while Q:
    x, y = Q.pop()
    for a, b in E[x]:
        Q += (a, b+y),
        C[a] = max(C[a], b+y)
Q, D, V = [(e, C[e])], 0, [0]*-~n
while Q:
    x, y = Q.pop()
    for a, b in R[x]:
        if y-b == C[a]:
            Q += (a, y-b+V[a]),
            V[a] += 1
            D += 1
print(C[e])
print(D)
