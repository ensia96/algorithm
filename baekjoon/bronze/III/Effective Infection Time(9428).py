n, *A = map(int, open(0).read().split())
for _ in ' '*n:
    a, b, c, d, A = *A[:4], A[4:]
    print(f"{[0.5*(12-a)/12+(d-b-1)+(d-1)/12, 0.5*(c-a)/(12-a+1)][b==d]:.4f}")
