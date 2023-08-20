for l in [*open(0)][1:]:
    n, m, l = map(int, l.split())
    print(-((n-m+l-1)//-m)+(l < 2))
