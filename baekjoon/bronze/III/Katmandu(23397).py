t, d, m, *A = map(int, open(0).read().split())
A = [0, *A, d]
print('NY'[t <= max(A[i+1]-A[i]for i in range(m+1))])
