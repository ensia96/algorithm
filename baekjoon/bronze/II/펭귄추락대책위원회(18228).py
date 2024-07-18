n, *A = map(int, open(0).read().split())
x = A.index(-1)
print(min(A[:x]) + min(A[x + 1 :]))
