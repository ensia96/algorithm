for l in [*open(i := 0)][:-1]:
    i += 1
    print(l[: -1 : i + 1])
