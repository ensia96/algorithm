for l in [*open(0)][1:]:
    n = int(l)
    print(n, len([i for i in range(n)if not n % -~i]))
