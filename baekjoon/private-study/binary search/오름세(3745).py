import bisect
for l in [*open(0)][1::2]:
    D = []
    for a in map(int, l.split()):
        t = bisect.bisect_left(D, a)
        D[t:t+1] = a
    print(len(D))
