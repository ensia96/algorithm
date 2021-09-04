l, t = lambda: map(int, input().split()), 0
n, k = l()
b, r = [*l()], [0]*n
while 1:
    b, r = b[-1:]+b[:-1], [0]+r[:-2]+[0]
    for i in range(n-1)[::-1]:
        if r[i]*b[i+1]*(not r[i+1]):
            r[i], r[i+1], b[i+1] = 0, r[i], b[i+1]-1
    r[0], b[0], t = *[(b[0], b[0]-1), (r[0], b[0])][not b[0]], t+1
    if b.count(0) >= k:
        exit(print(t))
