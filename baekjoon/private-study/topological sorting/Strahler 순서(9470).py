for _ in ' '*int(input()):
    k, m, p = map(int, input().split())
    E = [[]for _ in ' '*-~m]
    I, A, B = [0]*-~m, [1]*-~m, [0]*-~m
    for _ in ' '*p:
        a, b = map(int, input().split())
        E[a] += b,
        I[b] += 1
    Q = [i for i in range(1, m+1)if not I[i]]
    for q in Q:
        A[q] = 1
    while Q:
        q = []
        for x in Q:
            for a in E[x]:
                I[a] -= 1
                if A[x] > A[a]:
                    A[a], B[a] = A[x], 1
                elif A[x] == A[a]:
                    B[a] += 1
                if not I[a]:
                    A[a] = A[a]+(B[a] > 1)
                    q += a,
        Q = q
    print(k, A[-1])
