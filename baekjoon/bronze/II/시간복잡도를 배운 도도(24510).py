print(max(sum(map(l.count, ["for", "while"])) for l in [*open(0)][1:]))
