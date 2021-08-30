n, k = map(int, input().split())
q, l = [n], [0] * 100002

for p in q:
    if p == k:
        print(l[p])
        break
    for a in [p-1, p+1, p*2]:
        if 0 <= a <= 100002 and not l[a]:
            l[a] = l[p]
            if a == p*2:
                l[a] += 1
            q += [a]
