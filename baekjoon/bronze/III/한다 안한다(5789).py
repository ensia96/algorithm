for l in [*open(0)][1:]:
    x = len(l)//2
    print('Do-it'+'-Not'*(l[x] != l[x-1]))
