f = lambda: [*map(float, input().split())]
while (L := f())[0]:
    d, n = L
    n = int(n)
    L = [complex(*f())for _ in [0] * n]
    s = sum(all(abs(p - q) > d for q in L if p - q)for p in L)
    print(n - s, "sour,", s, "sweet")
