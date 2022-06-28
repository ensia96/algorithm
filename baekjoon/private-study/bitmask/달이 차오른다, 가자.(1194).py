n, m = map(int, input().split())
A = [input()for _ in ' '*n]
for i in range(n):
    for j in range(m):
        if A[i][j] == '0':
            Q = [(i, j, 0, 0)]
V = [[2**6*[1]for _ in ' '*m]for _ in ' '*n]
for i, j, k, d in Q:
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if(0 <= x < n)*(0 <= y < m) and A[x][y] != '#' and V[x][y][k]:
            V[x][y][k], f, t = 0, A[x][y], ord(A[x][y])
            if f in 'ABCDEF':
                if k & 1 << t-65:
                    Q += (x, y, k, d+1),
            elif f in 'abcdef':
                Q += (x, y, k | 1 << t-97, d+1),
            elif f == '1':
                exit(print(d+1))
            else:
                Q += (x, y, k, d+1),
print(-1)
