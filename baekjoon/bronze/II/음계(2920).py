*A, = map(int, input().split())
A, B = zip(*[(A[i] < A[i+1], A[i+1] < A[i])for i in range(7)])
print(['mixed', 'ascending', 'descending'][all(A)+2*all(B)])
