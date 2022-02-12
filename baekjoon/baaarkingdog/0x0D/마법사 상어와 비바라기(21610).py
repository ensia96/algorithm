l, Z = lambda: map(int, input().split()), lambda x: 0 <= x < n
n, m = l()
W = [[*l()]for _ in ' '*n]
C = {(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)}
D = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for _ in ' '*m:
    d, s = l()
    i, j = D[d-1]
    for z in ' '*s:
        C = {*map(lambda x: ((x[0]+i) % n, (x[1]+j) % n), C)}
    for x, y in C:
        W[x][y] += 1
    for x, y in C:
        for i, j in [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]:
            W[x][y] += Z(i)*Z(j) and bool(W[i][j])
    C = {(i, j)for i in range(n)for j in range(n)if W[i][j] > 1}-C
    for x, y in C:
        W[x][y] -= 2
print(sum(map(sum, W)))
