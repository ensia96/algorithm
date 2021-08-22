l = {tuple(map(int, input().split())): 1 for _ in range(int(input()))}
r = len(l)

for i in range(r):
    for j in range(r):
        if i == j:
            continue
        a, b = r[i]
        c, d = r[j]
        if a < c and b < d:
            l[r[i]] += 1

print(*l.values())
