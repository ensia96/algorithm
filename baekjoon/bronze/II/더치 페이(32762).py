n, m, *A = map(int, open(0).read().split())
print(sum(A[n*2+1::2])/n)
