for l in open(0):
    *A, = map(int, l.split())
    print(A[0]*A[1], *[a*b*c for a, b, c in zip(A, A[1:], A[2:])], A[-1]*A[-2])
