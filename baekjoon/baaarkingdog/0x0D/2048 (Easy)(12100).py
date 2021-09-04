n, g = int(input()), range
m = [[*map(int, input().split())] for _ in g(n)]
r, a = lambda m: [[m[n-1-j][i] for j in g(n)] for i in g(n)], 0


def c(l):
    a = [*filter(None, l)]
    for i in g(len(a)-1):
        if a[i] == a[i+1]:
            a[i], a[i+1] = a[i]*2, 0
    a = [*filter(None, a)]
    return a+[0]*(len(l)-len(a))


def e(t, m):
    global a
    if t == 0:
        a = max(a, max(map(max, m)))
        return
    for z in g(4):
        e(t-1, [c(l) for l in m])
        m = r(m)


e(5, m)
print(a)
