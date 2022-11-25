N, M = map(int, input().split())
*A, = map(int, input().split())


def f(x):
    t = []
    c = s = 0
    for a in A:
        if s+a > x:
            t += c,
            c = s = 0
        c += 1
        s += a
    return t+[c]


l, r = max(A), 100*N
while l < r:
    m = (l+r)//2
    if len(f(m)) > M:
        l = m+1
    else:
        r = m
t = f(l)
c = len(t)
print(l)
for i in range(c):
    while t[i] > 1 and M > c:
        print(1, end=' ')
        t[i] -= 1
        M -= 1
    print(t[i], end=' 'if c-1-i else'\n')
