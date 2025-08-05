n, *A = map(int, open(0).read().split())
print(*[sorted(T)[1] for T in zip(A, A[n:], A[2*n:])])
