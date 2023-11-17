*A, x = map(int, input().split())
a = b = 0
for i, j in sorted(zip(A[:3], A[3:]))[::-1]:
    for _ in range(j):
        a += i
        b += 1
        a >= x and exit(print(b))
print(0)
