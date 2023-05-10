for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    print(sum(range(1, a//b+1))+sum(range(a//b)))
