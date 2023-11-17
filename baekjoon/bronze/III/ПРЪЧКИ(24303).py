*A, x = map(int, input().split())
a = 0
for i, j in sorted(zip(A[:3], A[3:]))[::-1]:
    y = min(x//i, j)
    x -= i*y
    a += y
    x < 1 and exit(print(a))
print(0)
