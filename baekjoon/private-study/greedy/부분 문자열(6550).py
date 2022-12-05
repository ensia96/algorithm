for l in open(0):
    A, B = l.split()
    i = 0
    A += '1'
    for b in B:
        i += A[i] == b
    print('YNeos'[i != len(A)-1::2])
