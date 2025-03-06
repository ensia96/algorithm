_, *A, x = open(0).read().split()
A, B = A[::2], A[1::2]
t = A[B.index("teacher")]
print(sum(a >= t and a >= x for a in A) - 1)
