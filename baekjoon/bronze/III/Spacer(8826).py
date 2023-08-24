for l in [*open(0)][2::2]:
    n, e, w, s = map(l.count, 'NEWS')
    print(max(n, s)-min(n, s)+max(e, w)-min(e, w))
