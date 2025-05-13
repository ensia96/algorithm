n, m, *A = map(int, open(0).read().split())
print(sum(sum(i <= j for j in A[n:])for i in A[:n]))
