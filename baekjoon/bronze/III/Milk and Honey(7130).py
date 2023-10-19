m, h, n, *A = map(int, open(0).read().split())
print(sum(max(A[2*i]*m, A[2*i+1]*h)for i in range(n)))
