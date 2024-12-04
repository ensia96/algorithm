l, *L = open(0)
n, q = map(int, l.split())
C = [0] * -~n
for l in L:
    a, *A = map(int, l.split())
    if len(A):
        C[A[0]] = a < 2
    else:
        print(n - sum(C))
