n = int(input())
C, D = [[]for _ in ' '*-~n], [0]*-~n
for _ in ' '*~-n:
    p, c, w = map(int, input().split())
    C[p] += (c, w),
    C[c] += (p, w),
for i in range(1, -~n):
    q, v = [(i, 0)], [0]*-~n
    v[i] = 1
    for p, d in q:
        for c, w in C[p]:
            if not v[c]:
                v[c], D[i] = 1, max(D[i], w+d)
                q += [(c, d+w)]
print(max(D))
