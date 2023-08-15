i = 0
for l in [*open(0)][1:]:
    i += 1
    n, k, s = map(int, l.split())
    print(f'Case #{i}:', min(k-s+n-s, n)+k)
