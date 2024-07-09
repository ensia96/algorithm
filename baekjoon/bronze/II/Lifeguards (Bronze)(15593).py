f, M = lambda: map(int, input().split()), 1000
n, *_ = f()
W = [[*f()] for _ in " " * n]
T = [0] * M
for a, b in W:
    for i in range(a, b):
        T[i] += 1
print(max(sum(0 < T[i] - (a <= i < b) for i in range(M)) for a, b in W))
