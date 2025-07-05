n, *A = map(int, open(0).read().split())
for i in range(n):
    print(max(abs(A[i]-A[j])for j in range(n)))
