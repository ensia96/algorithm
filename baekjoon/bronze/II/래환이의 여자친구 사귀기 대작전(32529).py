n, m, *A = map(int, open(t := 0).read().split())
for i in range(n - 1):
    A[-i - 2] += A[-i - 1]
    if A[-i - 2] >= m:
        t = n - i
        break
print(t - 1)
