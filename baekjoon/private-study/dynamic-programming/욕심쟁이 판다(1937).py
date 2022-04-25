import sys
I, R = sys.stdin.readline, range
sys.setrecursionlimit(10**6)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def f(x, y):
    if D[x][y]:
        return D[x][y]
    D[x][y] = 1
    for i in R(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n)*(0 <= ny < n) and A[x][y] < A[nx][ny]:
            D[x][y] = max(D[x][y], f(nx, ny) + 1)
    return D[x][y]


n = int(I())
A = [[*map(int, I().split())]for _ in ' '*n]
D = [[0]*n for _ in ' '*n]
M = 0
for i in R(n):
    for j in R(n):
        M = max(M, f(i, j))
print(M)
