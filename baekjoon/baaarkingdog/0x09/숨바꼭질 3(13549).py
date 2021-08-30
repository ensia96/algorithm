n, k = map(int, input().split())
q, l = [n], [0] * 100002
l[n], w = 1, []

for p in q:
    for a in [p-1, p+1, p*2]:
        if 0 <= a < 100002 and not l[a]:
            v = l[p]
            if a != p*2:
                v += 1
            if a == k:
                w.append(v)
            l[a] = v
            q += [a]
print(min(w) - 1)
