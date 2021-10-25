import itertools as I
l, r = lambda: map(int, input().split()), range
n, p, a = int(input()), [*l()], 10000
g, b, A = lambda x: sum(p[i]for i in x), [[0]*n for _ in r(n)], {*r(n)}


def h(B):
    q = [B[0]]
    for i in q:
        for j in B:
            if b[i][j]*(j not in q):
                q += [j]
    return len(B) == len(q)


for i in r(n):
    for j in [*l()][1:]:
        b[i][j-1] = 1
for c in r(1, n//2+1):
    for C in I.combinations(r(n), c):
        D = A-set(C)
        a = [a, min(a, abs(g(C)-g(D)))][h([*C])*h([*D])]
print([a, -1][a == 10000])
