L, Q = lambda: map(int, input().split()), [1]
n, m = L()
E, G = [[]for _ in ' '*-~n], [0]*-~n
for _ in ' '*m:
    u, v = L()
    E[u] += v,
s = int(input())
for s in L():
    s-1 or exit(print('Yes'))
    G[s] = 1
while Q:
    c = Q.pop()
    E[c] or exit(print('yes'))
    for n in E[c]:
        if not G[n]:
            Q += n,
print('Yes')
