I, f = input, lambda x: [*map(int, x.split())]
while (A := I()) != '0':
    k, m = f(A)
    *A, = f(I())
    t = 0
    for _ in ' '*m:
        _, r, *C = f(I())
        t |= sum(map(A.count, C)) < r
    print('yneos'[t::2])
