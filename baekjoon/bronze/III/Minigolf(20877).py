n, *A = map(int, open(0).read().split())
print(sum(min(A[i], 7)-2-i % 2 for i in range(n)))
