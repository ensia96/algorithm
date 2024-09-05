for l in [*open(0).read().split()][1:]:
    t = "1" in l
    a, b = l.split("01"[t])
    print(len(a) % 2 ^ +(bool(b) or t))
