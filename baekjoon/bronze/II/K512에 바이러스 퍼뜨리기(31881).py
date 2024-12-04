l, *L = open(0)
n, q = map(int, l.split())
C = [0] * -~n
s = n
for l in L:
    a, *A = map(int, l.split())
    if len(A):
        s += C[A[0]] - (a < 2)
        C[A[0]] = a < 2
    else:
        print(s)
