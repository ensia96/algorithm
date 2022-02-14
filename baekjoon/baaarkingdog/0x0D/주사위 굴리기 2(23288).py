n, m, k = map(int, input().split())
B = [(*map(int, input().split()),) for _ in ' '*n]
D, L = [*range(1, 7)], [0]*2
M, d = lambda i, j, d: [(i, j+1), (i+1, j), (i, j-1), (i-1, j)][d], 0
g, A = lambda x, y: 0 <= x < n and 0 <= y < m, 0

for _ in ' '*k:
    if not g(*M(*L, d)):
        d = (d+2) % 4
    L = M(*L, d)
    if d == 0:
        D[0], D[2], D[3], D[5] = D[3], D[0], D[5], D[2]
    elif d == 1:
        D[0], D[1], D[4], D[5] = D[1], D[5], D[0], D[4]
    elif d == 2:
        D[0], D[2], D[3], D[5] = D[2], D[5], D[0], D[3]
    else:
        D[0], D[1], D[4], D[5] = D[4], D[0], D[5], D[1]
    i, j = L
    Q, V = [L], [[0]*m for _ in ' '*n]
    V[i][j] = 1
    for i, j in Q:
        for x, y in [M(i, j, k)for k in range(4)]:
            if g(x, y) and B[x][y] == B[i][j] and not V[x][y]:
                V[x][y] = 1
                Q += (x, y),
    A += len(Q)*B[i][j]
    x, y = D[-1], B[i][j]
    if x > y:
        d = (d+1) % 4
    if x < y:
        d = (d-1) % 4
print(A)
