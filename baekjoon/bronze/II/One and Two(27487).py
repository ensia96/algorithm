for l in [*open(0)][2::2]:
    (*A,) = map(int, l.split())
    x = y = A.count(2)
    if x < 2:
        print([1, -1][x])
    else:
        for i in range(len(A) - 1):
            y -= A[i] == 2
            if x // 2 == y:
                print(i)
