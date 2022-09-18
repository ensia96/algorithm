def f(x):
    A = 0
    for k in x:
        if x[k] and 1 in x[k]:
            A += (2 in x[k])+f(x[k])if 0 in x[k]else 1
    return A


for _ in ' '*int(input()):
    D = {}
    for _ in ' '*int(input()):
        T = D
        for s in input():
            T[s] = T = T.get(s, {})
            T[1] = 0
        T[2] = 0
    m = int(input())
    for _ in ' '*m:
        T = D
        for s in input():
            T[s] = T = T.get(s, {})
            T[0] = 0
    print(f(D)if m else 1)
