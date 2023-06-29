n, m, *L = map(int, open(0).read().split())
print(sum(L[i+1] <= L[i]-m for i in range(n-1)))
