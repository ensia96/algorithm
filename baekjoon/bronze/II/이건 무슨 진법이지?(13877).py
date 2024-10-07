for l in [*open(0)][1:]:
    a, b = l.split()
    print(a, 1 - ("9" in b) and int(b, 8), b, int(b, 16))
