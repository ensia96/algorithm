*A, = map(int, open(0).read().split())
t = sum((a > b)-(a < b)for a, b in zip(A[:10], A[10:]))
print('DAB'[(t > 0)+2*(t < 0)])
