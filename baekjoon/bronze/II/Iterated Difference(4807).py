*L, = open(i := 0)
for l in L[1::2]:
    *A, = map(int, l.split())
    n, c = len(A), 0
    while 1 < len({*A}) and c < 1001:
        A = [abs(A[i]-A[-~i % n])for i in range(n)]
        c += 1
    i += 1
    print(f'Case {i}:', [f"{c} iterations", 'not attained'][c > 1000])
