for l in [*open(0)][1:]:
    n, m = map(int, l.split())
    print((n+m)*(m-n+1)//2)
