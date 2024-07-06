for i in [*open(0)][1:]:
    n = int(i)
    print(sum((not n % -~i) for i in range(1, 1000)))
