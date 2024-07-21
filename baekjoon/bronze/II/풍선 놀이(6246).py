f = lambda: map(int, input().split())
n, q = f()
A = [[*f()] for _ in " " * q]
print([any(-~i % b == a for a, b in A) for i in range(n)].count(0))
