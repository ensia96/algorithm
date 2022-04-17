M = 8**8
n = int(input())
w = int(input())
A = [(*map(int, input().split()),)for _ in ' '*w]
B = [(n, n)]+A
A = [(1, 1)]+A
g, C = lambda A, B: abs(A[0]-B[0])+abs(A[1]-B[1]), [0]*w
D = [[-1]*-~w for _ in ' '*-~w]


def f(x, y):
    if (x == w)+(y == w):
        return 0
    if D[x][y] != -1:
        return D[x][y]
    D[x][y], m = M, max(x, y)+1
    D[x][y] = min(f(m, y)+g(A[x], A[m]), f(x, m)+g(B[y], B[m]))
    return D[x][y]


def F(x, y):
    if (x == w)+(y == w):
        return 0
    m = max(x, y)+1
    t = f(m, y)+g(A[x], A[m]) > f(x, m)+g(B[y], B[m])
    print(1+t)
    F(x if t else m, m if t else y)


print(f(0, 0))
F(0, 0)
