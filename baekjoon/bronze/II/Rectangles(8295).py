n, m, p = map(int, input().split())
print(
    sum(((i + j) * 2 >= p - 4) * (n - i) * (m - j) for i in range(n) for j in range(m))
)
