n = int(input())
A = [*map(int, input().split())]
E = [[]for _ in ' '*n]
for _ in ' '*~-n:
    a, b = map(int, input().split())
    E[a-1] += b-1,
    E[b-1] += a-1,
D = [[0]*2 for _ in ' '*n]
V = [0]*n
P = []


def f(x):
    D[x][1] = A[x]
    for i in E[x]:
        if not D[i][1]:
            D[x][0] += f(i)
            D[x][1] += D[i][0]
    return max(D[x])


def g(x, y):
    p = []
    if D[x][1] > D[x][0] and not V[y]:
        p += x+1,
        V[x] = 1
    for i in E[x]:
        if i != y:
            p += g(i, x)
    return p


print(f(0))
print(*sorted(g(0, 0)))
