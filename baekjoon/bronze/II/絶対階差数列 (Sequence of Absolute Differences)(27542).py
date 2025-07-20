n, *A = map(int, open(0).read().split())
while (n := n-1):
    A = [abs(A[i+1]-A[i])for i in range(n)]
print(*A)
