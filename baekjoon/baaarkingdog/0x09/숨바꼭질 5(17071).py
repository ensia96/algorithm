n, k = map(int, input().split())
m = int(5 * 10e4)
l = [0] * (m + 1)
q, l[n] = [n], 1

for p in q:
    v = k + sum(range(l[p]))
    if v > m:
        print(-1)
        break
    elif l[v]:
        print(l[v] - 1)
        break
    for a in [p-1, p+1, p*2]:
        if 0 < a <= m and not l[a]:
            l[a] = l[p] + 1
            q += [a]
