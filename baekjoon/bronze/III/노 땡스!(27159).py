a, *A = map(int, open(0).read().split())
A = [0]+sorted(A)
print(sum((A[i]+1 != A[i+1])*A[i+1]for i in range(a)))
