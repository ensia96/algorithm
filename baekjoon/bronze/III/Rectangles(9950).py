for l in [*open(0)][:-1]:
    l, w, a = map(int, l.split())
    print(l+(l == 0 and a//w), w+(w == 0 and a//l), a+(a == 0 and l*w))
