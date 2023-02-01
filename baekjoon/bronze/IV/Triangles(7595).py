for l in open(0):
    i, *_ = map(int, l.split())
    for j in range(i):
        print('*'*-~j)
