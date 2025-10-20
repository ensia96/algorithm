for l in [*open(0)][1:]:
    a, b = l.split()
    t = 1
    for i in range(int(a)):
        t *= -~i
    print(str(t).count(b))
