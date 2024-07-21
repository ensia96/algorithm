f = lambda: map(int, input().split())
n, q = f()
T = [0] * n
for _ in " " * q:
    a, b = f()
    for i in range(a - 1, n, b):
        T[i] = 1
print(T.count(0))
