i, g = input, range
n = int(i())
m = [[*map(int, i().split())] for _ in g(n)]
r, a = lambda m: [[m[n-1-j][i] for j in g(n)] for i in g(n)], 0


def c(l):
    a = [i for i in l if i]
    for i in g(len(a)-1):
        if a[i] == a[i+1]:
            a[i], a[i+1] = a[i]*2, 0
    a = [i for i in a if i]
    return a+[0]*(len(l)-len(a))


def e(t, m):
    global a
    if t == 0:
        return max(map(max, m))
    for z in g(4):
        a = max(a, e(t-1, [c(l) for l in m]))
        m = r(m)
    return a


print(e(5, m))
