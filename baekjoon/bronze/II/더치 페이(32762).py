n, *A = map(int, open(0).read().split())
print(sum(A[n*2+2::2])/n)
