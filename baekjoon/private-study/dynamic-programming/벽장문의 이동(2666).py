n = int(input())
a, b = map(int, input().split())
m = int(input())
A = [~-int(input())for _ in ' '*m]
D = [[m*[-1]for _ in ' '*n]for _ in ' '*n]


def f(x, y, z):
    if z == m:
        return 0
    elif D[x][y][z] == -1:
        D[x][y][z] = min(abs(x-A[z])+f(A[z], y, z+1),
                         abs(y-A[z])+f(x, A[z], z+1))
    return D[x][y][z]


print(f(a-1, b-1, 0))
