for l in [*open(0)][2::2]:
    A = [0]
    for i in map(int, l.split()):
        A += (A[-1] + i,)
    print((A[-1] // 2 in A and A.index(A[-1] // 2)) - (len(A) > 3))
