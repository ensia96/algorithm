for l in [*open(0)][1:]:
    n, b = map(int, l.split())
    s = ""
    while n:
        n, r = divmod(n, b)
        s += "0123456789ABCDEF"[r]
    print(+(s == s[::-1]))
