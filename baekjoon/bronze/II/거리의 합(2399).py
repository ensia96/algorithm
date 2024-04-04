n, *A = map(int, open(0).read().split())
n = range(n)
print(sum(abs(A[i]-A[j])for i in n for j in n))
