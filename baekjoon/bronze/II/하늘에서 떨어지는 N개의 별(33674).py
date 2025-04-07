n, d, k, *A = map(int, open(0).read().split())
T = [0] * n
x = 0
for _ in " " * (d - 2):
    for i in range(n):
        T[i] += A[i]
        if T[i] > k:
            T[i] = 0
            x += 1
print(x)
