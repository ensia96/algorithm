for l in [*open(0)][1:]:
    n, a, *A, b = map(int, l.split())
    x = (b-a)//(n-2)
    for i in range(n-2):
        if A[i] != a+x*-~i:
            print(i+2)
            break
