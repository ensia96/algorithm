f = lambda: [*map(int, input().split())]
n, q = f()
C = [0] * -~n
for _ in " " * q:
    a, *A = f()
    if len(A):
        C[A[0]] = a < 2
    else:
        print(n - sum(C))
