l, _ = lambda: map(int, input().split()), 0
n, m, a = *l(), [*l()]
for _ in range(m):
    a.sort()
    a[0] = a[1] = a[0]+a[1]
print(sum(a))
