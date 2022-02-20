I, R = input, range
for _ in ' '*int(I()):
    h, w = map(int, I().split())
    T, V = ['.'*(w+2)], [[0]*(w+2) for _ in ' '*(h+2)]
    A, B = 0, T+[f'.{I()}.'for _ in ' '*h]+T
    K, Q, T = {i: 1 for i in I()+'.$'}, [(0, 0)], {}
    while Q:
        q = []
        for i, j in Q:
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x <= h+1 and 0 <= y <= w+1 and B[x][y] != '*' and not V[x][y]:
                    t, V[x][y] = B[x][y], 1
                    A += (t == '$')
                    if t.islower():
                        K[t] = 1
                    elif K.get(t.lower()):
                        q += (x, y),
                    elif t.isupper():
                        T[t] = [(x, y)]
        for t in [t for t in T if K.get(t.lower())]:
            q += T.pop(t)
        Q = q
    print(A)
