for l in [*open(0)][:-1]:
    n = int(l)
    print(n//100*(100-10*((n > 1e6)+(n > 5e6))))
