import sys
sys.setrecursionlimit(10**6)
n = int(input())
A = [[*map(int, input().split())]for _ in ' '*n]
D = [[0]*n for _ in ' '*n]
N = range(n)
R = 0


def f(i, j):
    if D[i][j]:
        return D[i][j]
    D[i][j] = 1
    for x, y in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
        if (0 <= x < n)*(0 <= y < n) and A[i][j] < A[x][y]:
            D[i][j] = max(D[i][j], f(x, y)+1)
    return D[i][j]


for i in N:
    for j in N:
        R = max(R, f(i, j))
print(R)
