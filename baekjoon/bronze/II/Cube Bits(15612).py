for l in [*open(0)][1:]:
    l = int(l)
    t = ''
    while l:
        t = str(l % 3) + t
        l //= 3
    print(t or 0)
