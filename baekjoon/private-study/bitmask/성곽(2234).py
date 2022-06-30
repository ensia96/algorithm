n, m = map(int, input().split())
N, M = range(n), range(m)
A = [[*map(int, input().split())]for _ in M]
B, C = [n*[0]for _ in M], [n*[0]for _ in M]
a = b = c = 0
for i in M:
    for j in N:
        if not B[i][j]:
            Q, a = [(i, j)], a+1
            for x, y in Q:
                B[x][y], D = a, [(x, y-1), (x-1, y), (x, y+1), (x+1, y)]
                for k in range(4):
                    if not A[x][y] & 1 << k:
                        p, q = D[k]
                        if (0 <= p < m)*(0 <= q < n) and not B[p][q]:
                            Q += (p, q),
            b = max(b, len(Q))
            for x, y in Q:
                C[x][y] = len(Q)
for i in M:
    for j in N:
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if (0 <= x < m)*(0 <= y < n) and B[i][j] != B[x][y]:
                c = max(c, C[i][j]+C[x][y])
print(a, b, c, sep='\n')
