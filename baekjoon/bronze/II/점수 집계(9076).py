n, *A = open(0)
for a in A:
    m, a, b, c, M = sorted(map(int, a.split()))
    print([a+b+c, 'KIN'][c-a > 3])
