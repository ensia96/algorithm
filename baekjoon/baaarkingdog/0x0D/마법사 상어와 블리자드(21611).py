L, d = lambda: map(int, input().split()), 0
n, m = L()
h, l = (n-1)//2, n**2-1
B, O = [[0]*n for _ in ' '*n], [(0, 0)]
B[0][0] = B[h][h] = 1
A = 0
while len(O) < l:
    i, j = O[-1]
    x, y = [(i, j+1), (i+1, j), (i, j-1), (i-1, j)][d]
    if 0 <= x < n and 0 <= y < n and not B[x][y]:
        B[x][y] = 1
        O += [(x, y)]
    else:
        d = (d+1) % 4
O, B = O[::-1], [[*L()]for _ in ' '*n]


def D(d, s):
    i = j = h
    for _ in ' '*s:
        i, j = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)][d-1]
        B[i][j] = 0


def M():
    T = [B[i][j]for i, j in O if B[i][j]]
    t = len(T)
    for i in range(l):
        x, y = O[i]
        B[x][y] = t > i and T[i]


def C():
    T, R = [B[i][j]for i, j in O], []
    i = j = 0
    for x in T:
        if i-x:
            R += (j, i),
            i, j = x, 1
        else:
            j += 1
    return R[1:]


def E():
    global A
    x = f = 0
    for i, j in C():
        if i > 3:
            f, A = 1, A+i*j
            for a, b in O[x:x+i]:
                B[a][b] = 0
        x += i
    M(), f and E()


def V():
    T = []
    for i in C():
        T += i
    T += [0]*l
    for i in range(l):
        x, y = O[i]
        B[x][y] = T[i]


for _ in ' '*m:
    d, s = L()
    D(d, s)
    M()
    E()
    V()
print(A)
