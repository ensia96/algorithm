for l in [*open(0)][1:]:
    n, *P = map(int, l.split())
    A = sum(P) / n
    print(f"{A + 1e-12:.3f} {sum(p > A for p in P) * 100 / n + 1e-12:.3f}%")
