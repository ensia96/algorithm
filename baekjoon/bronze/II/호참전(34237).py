f = lambda: [*map(int, input().split())]
n, m = f()
D = {}
for _ in ' ' * n:
    a, b = f()
    D[a] = D.get(a, []) + [b]
for _ in ' ' * m:
    g, x, y = f()
    print(sum(sum(y <= d <= g - i for d in D[i])for i in D if i >= x))
