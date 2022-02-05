n, m = map(int, input().split())
n += 1
E = []
for _ in ' '*-~m:
    i, j, w = map(int, input().split())
    E += (not w, i, j),


def F(r):
    def f(x):
        if x != P[x]:
            P[x] = f(P[x])
        return P[x]
    P, L = [*range(n+1)], [0]*n
    a = e = 0
    for w, i, j in sorted(E, reverse=r):
        i, j = f(i), f(j)
        if i == j:
            continue
        a, e = a+w, e+1
        if e == n-1:
            return a**2
        if L[i] < L[j]:
            i, j = j, i
        P[i], L[i] = j, L[i]+1


print(F(1)-F(0))
