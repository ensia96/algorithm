n, *A = map(int, open(0).read().split())
print(sum((A[i]+A[i+1])/2*A[n+i+1]for i in range(n)))
