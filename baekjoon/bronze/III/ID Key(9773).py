for l in [*open(0)][1:]:
    n = sum(map(int, l[:-1]))+int(l[-4:-1])*10
    print(f"{(n%10000)+1000*(n<1000):04d}")
