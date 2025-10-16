f = lambda: [*map(int, input().split())]
n, m = f()
T = f()
print(min((-sum(a == b for a, b in zip(T, f())), -~i)for i in range(n))[1])
