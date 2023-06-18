t = 0
for l in [*open(0)][1:]:
    n, *A = map(int, l.split())
    B = []
    print(f'Case {t}:', n-1, *[A[i]*(n-i)for i in range(n)])
    t += 1
