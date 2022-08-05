for _ in ' '*int(input()):
    n = int(input())
    N = range(1, n+1)
    I = [0]*-~n
    A = [*map(int, input().split())]
    for i in range(1, n):
        for j in range(i, n):
            I[A[j]] += 1
    X = I[:]
    m = int(input())
    for _ in ' '*m:
        a, b = map(int, input().split())
        t = I[a] > I[b]
        X[a] += 1*(1-2*t)
        X[b] += 1*(2*t-1)
    Q = [i for i in N if not X[i]]
    A = []
    if not Q:
        print("IMPOSSIBLE")
        continue
    while Q:
        if len(Q) > 1:
            A = ['?']
            break
        A += Q.pop(),
        for i in N:
            X[i] -= 1
            if X[i] == 0:
                Q += i,
    print(*A)
