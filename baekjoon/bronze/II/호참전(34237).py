(n, m), *L = [[*map(int, l.split())]for l in open(0)]
for g, x, y in L[n:]:
    print(sum(y <= b <= g - a <= g - x for a, b in L[:n]))
