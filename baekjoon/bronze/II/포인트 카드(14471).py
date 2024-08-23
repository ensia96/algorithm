f = lambda: map(int, input().split())
n, m = f()
A = [max(n - [*f()][0], 0) for _ in " " * m]
print(sum(A) - max(A))
