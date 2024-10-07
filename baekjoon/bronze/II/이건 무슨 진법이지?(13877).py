for l in [*open(0)][1:]:
    a, b = l.split()
    print(a, 0 if "9" in b else int(b, 8), b, int(b, 16))
