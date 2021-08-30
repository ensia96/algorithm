n, k = map(int, input().split())
q, l = [n], [0] * 100002
l[n], w = 1, []

for p in q:
    for a, t in [(p-1, 1), (p+1, 1), (p*2, 0)]:
        if 0 <= a < 100002 and not l[a]:
            v = l[p] + t
            if a == k:
                w += [v]
            else:
                l[a] = v
                q += [a]

print(min(w) - 1)
