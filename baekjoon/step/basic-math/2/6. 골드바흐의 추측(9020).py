l = map(int, [*open(0)][1:])

m = max(l) + 1
a = [1 for _ in range(0, m)]

for i in range(2, m):
    if a[i]:
        for j in range(2 * i, m + 1, i):
            a[j] = 0

for n in l:
    for i in range(2, n // 2):
        b = n - i
        if b > 1 and a[b]:
            x, y = i, b
    print(x, y)
