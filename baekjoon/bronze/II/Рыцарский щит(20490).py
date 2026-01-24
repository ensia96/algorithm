*a, = map(int, open(0).read().split())
print(sum(a) - 2 * min(max(a[:3]), max(a[3:])))
