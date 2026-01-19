R = range
n, m, *L = map(int, open(0).read().split())
print(min(sum(L[k * m + l] * (abs(i - k) + abs(j - l))for k in R(n)
      for l in R(m)if (k, l) != (i, j))for i in R(n)for j in R(m)))
