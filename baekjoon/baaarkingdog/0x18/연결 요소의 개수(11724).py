n, m = map(int, input().split())
E, V, A = [[]for _ in ' '*n], [0]*n, 0
for _ in ' '*m:
    u, v = map(int, input().split())
    E[u-1] += [v-1]
    E[v-1] += [u-1]
for v in range(n):
    if V[v]:
        continue
    q, V[v], A = [v], 1, A+1
    for i in q:
        for j in E[i]:
            if not V[j]:
                q += [j]
                V[j] = 1
print(A)
