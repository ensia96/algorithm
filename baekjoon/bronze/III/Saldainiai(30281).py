n, *A = map(int, open(0).read().split())
A.sort()
print(max(s//2*-~-(s % 2)for s in [sum(A[i:])for i in range(n)]))
