for l in [*open(0)][1:]:
    t, *l, _ = l
    C = [1]
    for i in range(len(l)):
        if t[-1] != l[i]:
            t += l[i]
            C += (0,)
        C[-1] += 1
    print(*[y for x in zip(C, t) for y in x])
