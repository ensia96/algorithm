for l in [*open(0)][1:]:
    a, b = l.split()
    print(a, int(b, 8) if max(b) < "8" else 0, b, int(b, 16))
