def f(n, s, e, t, v):
    if s == t == e:
        T[n] += v
        C[n] = t
    elif t >= s and e >= t:
        m = (s+e)//2
        T[n] = f(n*2, s, m, t, v)+f(n*2+1, m+1, e, t, v)
    return T[n]


def g(n, s, e, t):
    if s == e:
        T[n] -= 1
        print(C[n])
    else:
        l, m = T[n*2], (s+e)//2
        g(n*2+1, m+1, e, t-T[n*2])if l < t else g(n*2, s, m, t)
        T[n] = T[n*2]+T[n*2+1]
    return T[n]


M = 10**6
T = M*4*[0]
C = M*4*[0]
for _ in ' '*int(input()):
    a, *A = map(int, input().split())
    f(1, 1, 1000000, *A)if a-1 else g(1, 1, 1000000, *A)
