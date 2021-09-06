import sys
i = sys.stdin.readline
l, _ = lambda: [*map(int, i().split())], 0

for _ in range(int(i())):
    i()
    a, b = {}, {}
    for k in l():
        a[k] = a.get(k, 0)+1
    for k in l():
        b[k] = b.get(k, 0)+1
    print(sum(a[i] * b[j] for i in a for j in b if i > j))
