for l in [*open(0)][:-1]:
    y, n, a = map(l.count, "YNA")
    print(["need quorum", ["tie", "no", "yes"][(y < n) + 2 * (y > n)]][len(l) // 2 > a])
