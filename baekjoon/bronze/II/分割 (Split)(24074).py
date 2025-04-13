n, *A = map(int, open(0).read().split())
t = A.index(max(A))
print(sum(A[:t]))
print(sum(A[t + 1 :]))
