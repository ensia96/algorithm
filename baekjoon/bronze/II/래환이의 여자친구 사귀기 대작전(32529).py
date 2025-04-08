n, m, *A = map(int, open(0).read().split())
x = sum(A)
i = 0
while x >= m:
    x -= A[i]
    if x <= m:
        exit(print(i + 1))
    i += 1
print(-1)
