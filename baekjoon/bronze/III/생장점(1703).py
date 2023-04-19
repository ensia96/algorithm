for l in [*open(0)][:-1]:
    a, *A = map(int, l.split())
    x = 1
    for i in range(a):
        x = x*A[2*i]-[2*i+1]
    print(x)
