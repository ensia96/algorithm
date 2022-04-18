import collections as C
S = str
d, s = lambda n: n*2 % 10000, lambda n: (n-1) % 10000
l, r = lambda n: int(S(n)[1:]+S(n)[:1]), lambda n: int(S(n)[-1:]+S(n)[:-1])

for _ in ' '*int(input()):
    a, b = map(int, input().split())
    D = [0]*10000
    D[a] = ''
    Q = C.deque([a])
    while not D[b]:
        p = Q.popleft()
        q = [d(p), s(p), l(p), r(p)]
        for i in range(4):
            x = q[i]
            if D[x]:
                continue
            D[x] = D[p]+'DSLR'[i]
            if x == b:
                break
            Q += x,
    print(D[b])
