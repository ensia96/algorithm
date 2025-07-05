n, *A = map(int, open(0).read().split())
x, y = min(A), max(A)
for i in range(n):
    print(max(abs(A[i]-x), abs(A[i]-y)))
