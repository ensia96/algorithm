n, m, k, *A = map(int, open(0).read().split())
print(n-m-k)
print(*{*range(1, n+1)}-{*A})
