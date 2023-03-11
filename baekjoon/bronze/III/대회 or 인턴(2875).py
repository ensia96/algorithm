n, m, k = map(int, input().split())
while k:
    if n-1 > m*2:
        n -= 1
    else:
        m -= 1
    k -= 1
print(min(n//2, m))
