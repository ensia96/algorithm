n = int(input())
N = 1 << n
G = [[*map(int, input().split())]for _ in ' '*n]
M = 9**11
D = [[M]*N for _ in ' '*n]


def f(x, v):
    if v == N-1:
        return G[x][0] or M
    if D[x][v] != M:
        return D[x][v]
    for i in range(1, n):
        if not G[x][i] or v & (1 << i):
            continue
        D[x][v] = min(D[x][v], f(i, v | (1 << i))+G[x][i])
    return D[x][v]


print(f(0, 1))
