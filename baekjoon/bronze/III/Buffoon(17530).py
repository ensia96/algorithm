n, *A = map(int, open(0))
print('SN'[any(A[0] < A[i]for i in range(1, n))])
