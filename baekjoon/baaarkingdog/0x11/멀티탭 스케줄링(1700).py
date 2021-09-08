l, a = lambda: map(int, input().split()), 0
n, k = l()
E, D, M = [*l()], {}, []
for i in range(k)[::-1]:
    e = E[i]
    D[e] = D.get(e, [])+[i]
for e in E:
    D[e].pop()
    M.sort(key=lambda e: min(D[e] or [101]))
    if e not in M:
        a, M = a+bool(len(M) == n and M.pop()), M+[e]
print(a)
