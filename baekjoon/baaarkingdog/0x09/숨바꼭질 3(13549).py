n, k = map(int, input().split())
q, l = [n], [0] * 100002
l[n] = 1

for p in q:
    if l[k]:
        print(l[k] - 1)
        break
    for a, t in [(p*2, 0), (p-1, 1), (p+1, 1)]:
        if 0 <= a < 100002 and not l[a]:
            l[a] = l[p] + t
            q += [a]
