T = {}
for _ in ' '*int(input()):
    C = T
    for s in input().split('\\'):
        C[s] = C = C.get(s, {})


def f(x, y):
    for k in sorted(x):
        print(' '*y+k)
        x[k] and f(x[k], y+1)


f(T, 0)
