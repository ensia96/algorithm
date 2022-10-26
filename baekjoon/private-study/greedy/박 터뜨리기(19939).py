n, k = map(int, input().split())
x = sum(range(k+1))
print(-1 if n < x else k-(not(n-x) % k))
