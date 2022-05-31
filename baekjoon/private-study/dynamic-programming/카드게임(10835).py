n = int(input())
L = [*map(int, input().split())]
R = [*map(int, input().split())]
D = [[-1]*n for _ in ' '*n]


def f(i, j):
    if i == n or j == n:
        return 0
    if D[i][j]+1:
        return D[i][j]
    D[i][j] = max(f(i+1, j+1), f(i+1, j), (L[i] > R[j]) and (f(i, j+1)+R[j]))
    return D[i][j]


print(f(0, 0))
