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
    q = [(a, b+y)for x, y in Q for a, b in E[x]]
    for x, y in q:
        C[x] = max(C[x], y)
    Q = q
Q, q = [(e, C[e])], set()
while Q:
    x, y = Q.pop()
    for a, b in R[x]:
        if y-b == C[a]:
            Q += (a, y-b),
            q.add((a, b))
print(C[e])
print(len(q))
