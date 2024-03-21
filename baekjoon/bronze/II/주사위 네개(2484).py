P, X = print, 0
for l in [*open(0)][1:]:
    *A, = map(int, l.split())
    T = sorted({t: A.count(t)
               for t in {*A}}.items(), key=lambda t: t[::-1])[::-1]
    l = len(T)
    x = T[0][0]
    if l == 3:
        x = 10+x
    elif l > 1:
        if T[0][1] > 2:
            x = 100+x*10
        else:
            x = 20+(x+T[1][0])
    else:
        x = 500+x*50
    X = max(X, x)
print(X*100)
