import sys
i, r = sys.stdin.readline, range
n, u = int(i()), [-1, 0, 1]
m, d = [[*map(int, i().split())] for _ in r(n)], {k: 0 for k in u}


def c(t, x=0, y=0):
    if t == 1:
        v = m[x][y]
        d[v] += 1
        return v
    t, l = t // 3, []
    for i in r(3):
        for j in r(3):
            if x+(t*i) < n and y+(t*j) < n:
                l += [c(t, x+(t*i), y+(t*j))]
    for v in u:
        a = [*filter(lambda x: x == v, l)]
        if a == l:
            d[v] -= 8
            return v


c(n)
print('\n'.join(map(str, d.values())))
