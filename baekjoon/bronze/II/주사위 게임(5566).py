n, m, *A = map(int, open(0).read().split())
B, A = A[:n], A[n:]
x = y = 0
for a in A:
    y += 1
    x += a
    if x >= n:
        break
    x += B[x % n]
print(y)
