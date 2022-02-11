l, A = lambda: map(int, input().split()), 0
n, m = l()
B = [[*l()]for _ in ' '*n]
C = [(i//n, i % n)for i in range(n**2)]


def f():
    A, D, V = [], {}, [[0]*n for _ in ' '*n]
    for i, j in C:
        if V[i][j] or B[i][j] < 1:
            continue
        V[i][j], Q, R, c = 1, [(i, j)], [], B[i][j]
        for x, y in Q:
            for p, q in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= p < n and 0 <= q < n and not V[p][q] and B[p][q] in (0, c):
                    B[p][q] or R.append((p, q))
                    V[p][q] = 1
                    Q += (p, q),
        for p, q in R:
            V[p][q] = 0
        A += (-len(Q), -len(R), -i, -j),
        D[(i, j)] = Q
    if not A:
        return
    a, b, c, d = sorted(A)[0]
    if -a < 2:
        return
    for i, j in D[(-c, -d)]:
        B[i][j] = -2
    return a**2


def g():
    for i, j in C[::-1]:
        if B[i][j]+2:
            continue
        Q = [(i, j)]
        for x, y in Q:
            if B[x][y] >= 0:
                break
            if 0 <= x-1 and B[x-1][y]+1:
                Q += (x-1, y),
        B[i][j], B[x][y] = B[x][y], -2


while 1:
    s = f()
    if not s:
        break
    A = A+s
    g()
    B = [*map(list, zip(*B))][::-1]
    g()
print(A)
