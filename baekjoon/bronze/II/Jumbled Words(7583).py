while (A := input()) != "#":
    print(*["".join([i[0], *i[-2:0:-1]]) + (len(i) > 1) * i[-1] for i in A.split()])
