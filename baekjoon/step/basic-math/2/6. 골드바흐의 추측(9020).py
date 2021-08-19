l = map(int, [*open(0)][1:])

m = max(l) + 1
a = [1 for _ in range(0, m)]

for i in range(2, m):
    if a[i]:
        for j in range(2 * i, m, i):
            a[j] = 0

for n in l:
    for i in range(2, n // 2):
        if a[i]:
            b = n - i
            if a[b]:
                x, y = i, b
    print(x, y)
