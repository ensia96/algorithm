n, *A = map(int, open(0).read().split())
print(min(sum(A), n-sum(A)))
