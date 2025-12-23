n, *L = open(t := 0)
for a, b in zip(L[::2], L[1::2]):
    n, l, h, *F = map(int, (a + b).split())
    F = [i for i in range(l, h + 1)if not any(i % f and f % i for f in F)]
    t += 1
    print(f"Case #{t}:", min(F)if F else 'NO')
