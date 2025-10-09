for l in [*map(int, open(0))][1:]:
    t = ''
    while l:
        t = str(l % 3) + t
        l //= 3
    print(t or 0)
