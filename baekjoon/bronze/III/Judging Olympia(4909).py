for l in [*open(0)][:-1]:
    *A, = map(int, l.split())
    x = sum(A)-max(A)-min(A)
    print(x/4 if x % 4 else int(x))
