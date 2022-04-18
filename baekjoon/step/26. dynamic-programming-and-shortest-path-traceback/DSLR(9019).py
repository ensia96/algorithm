import collections as C
M, m = 10000, 1000
for _ in ' '*int(input()):
    a, b = map(int, input().split())
    D = [0]*10000
    D[a] = ''
    Q = C.deque([a])
    while D[b] == 0:
        p = Q.popleft()
        q = [p*2 % M, (p-1) % M, p % m*10+p//m, p % 10*m+p//10]
        for i in range(4):
            x = q[i]
            if D[x] == 0:
                D[x] = D[p]+'DSLR'[i]
                Q += x,
    print(D[b])
