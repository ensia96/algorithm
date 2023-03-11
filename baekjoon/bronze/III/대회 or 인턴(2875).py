n, m, k = map(int, input().split())
for _ in ' '*k:
    if n-1 < m*2:
        m -= 1
    else:
        n -= 1
print(min(n//2, m))
