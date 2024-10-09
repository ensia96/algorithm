n, m, *A = map(int, open(0).read().split())
y = 0
for i in range(n):
    x = 0
    for t in A[-m:]:
        x ^= A[2 * i + x] <= t
    y += A[2 * i + x]
print(y)
