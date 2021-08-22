l = [tuple(map(int, input().split())) for _ in range(int(input()))]
r = len(l)
v = {k: 1 for k in l}

for i in range(r):
    for j in range(r):
        if i == j:
            continue
        a, b = l[i]
        c, d = l[j]
        if a < c and b < d:
            v[l[i]] += 1

print(*v.values())
