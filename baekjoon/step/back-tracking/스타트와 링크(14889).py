n = int(input())
s = [[*map(int, input().split())] for _ in range(n)]
g = {*range(n)}
l, v = lambda x: sum(s[i][j] for i in x for j in x), [1]*n


def f(a, c):
    if c == n:
        return abs(l(g-set(a))-l(a))
    r = 10**8
    for i in range(n):
        if v[i]:
            v[i] = 0
            r = min(r, f(a+[i], c+2))
            v[i] = 1
    return r


print(f([], 0))
