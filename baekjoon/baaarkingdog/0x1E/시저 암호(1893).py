for _ in ' '*int(input()):
    A, W, S = input(), input(), input()
    n, m = len(A), len(W)
    D, R = {A[i]: A[i-1]for i in range(n)}, []
    f, j = [0]*m, 0
    for i in range(1, m):
        while j and W[i] != W[j]:
            j = f[j-1]
        if W[i] == W[j]:
            j += 1
            f[i] = j
    for i in range(n):
        c = 0
        for k in range(len(S)):
            while j and S[k] != W[j]:
                j = f[j-1]
            j += S[k] == W[j]
            if j == m:
                j = f[j-1]
                c += 1
        if c == 1:
            R += i,
        S = ''.join(D[s]for s in S)
    r = len(R)
    if r == 0:
        print('no solution')
    elif r == 1:
        print('unique: %d' % R[0])
    else:
        print('ambiguous: ', end='')
        print(*R)
