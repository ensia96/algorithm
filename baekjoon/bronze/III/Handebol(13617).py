n, m, *A = map(int, open(0).read().split())
print(sum(all(A[m*i:m*i+m])for i in range(n)))
