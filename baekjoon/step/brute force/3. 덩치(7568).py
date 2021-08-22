l = [tuple(map(int, input().split())) for _ in range(int(input()))]
r, v = len(l), [1 for _ in l]

for i in range(r):
    for j in range(r):
        if i == j:
            continue
        a, b = l[i]
        c, d = l[j]
        if a < c and b < d:
            v[i] += 1

print(*v)
