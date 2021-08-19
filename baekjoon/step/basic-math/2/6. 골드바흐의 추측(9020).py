l = map(int, [*open(0)][1:])

m = max(l) + 1
a = [0, 0] + [1 for _ in range(m)]

for i in range(2, m):
    if a[i]:
        for j in range(2 * i, m + 1, i):
            a[j] = 0

for n in l:
    x = n // 2
    y = x
    for i in range(n):
        if a[x] and a[y]:
            print(x, y)
            break
        x -= 1
        y += 1
