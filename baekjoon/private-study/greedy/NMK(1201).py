n, m, k = map(int, input().split())
print(*[j for i in range(m)for j in range(min(-~i*k, n-m+-~i),
      min(i*k, n-m+i), -1)]if m+k-1 <= n <= m*k else[-1])
