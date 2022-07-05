n, l, r, x = map(int, input().split())
A = [*map(int, input().split())]
R = 0
for i in range(1 << n):
    s, m, M = 0, r, 0
    for j in range(n):
        if i & 1 << j:
            m, M = min(m, A[j]), max(M, A[j])
            s += A[j]
    R += l <= s <= r and M-m >= x
print(R)
