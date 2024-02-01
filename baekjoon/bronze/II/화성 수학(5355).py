_, *A = open(0)
for a in A:
    n, *O = a.split()
    n = float(n)
    for o in O:
        if o == '@':
            n *= 3
        if o == '%':
            n += 5
        if o == '#':
            n -= 7
    print(f"{n:.2f}")
