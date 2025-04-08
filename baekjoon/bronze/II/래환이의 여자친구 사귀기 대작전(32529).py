n, m, *A = map(int, open(t := 0).read().split())
A += (0,)
for i in range(n):
    A[-i - 2] += A[-i - 1]
    if A[-i - 2] >= m:
        t = n - i + 1
        break
print(t - 1)
