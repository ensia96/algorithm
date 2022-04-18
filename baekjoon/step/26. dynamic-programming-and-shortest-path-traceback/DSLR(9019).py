import collections as C
d, s = lambda n: n*2 % 10000, lambda n: (n-1) % 10000


def l(n):
    s = str(n)
    while len(s) < 4:
        s = '0'+s
    return int(s[1:]+s[:1])


def r(n):
    s = str(n)
    while len(s) < 4:
        s = '0'+s
    return int(s[-1:]+s[:-1])


for _ in ' '*int(input()):
    a, b = map(int, input().split())
    D = [0]*10000
    D[a] = 'x'
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
    print(D[b][1:])
