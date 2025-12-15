A, *L = open(0)
for l in L:
    C = ''.join('XYG'[2 * (A[i] == l[i]) or l[i] in A]for i in range(5))
    print([C, 'WINNER'][f := C == 'GGGGG'])
    f and exit()
