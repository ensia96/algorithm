n, k = map(int, input().split())
m = int(5 * 10e4)
l = [0] * (m + 1)
q, l[n], r = [n], 1, -1

for p in q:
    if p == k + sum(range(l[p])):
        r = l[p]
        break
    for a in [p-1, p+1, p*2]:
        if 0 < a <= m and not l[a]:
            l[a] = l[p] + 1
            q += [a]
print(r)
