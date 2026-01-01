for l in [*open(0)][1:]:
    c, i = 0, int(l)
    while i > 1:
        c += i % 2
        i -= i // 2
    print(c)
