for l in [*open(0)][:-1]:
    (*A,) = filter(str.isalpha, l)
    len(A) == len({*A}) and print(l[:-1])
