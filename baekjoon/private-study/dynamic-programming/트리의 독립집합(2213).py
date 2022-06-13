n = int(input())
A = [*map(int, input().split())]
E = [[]for _ in ' '*n]
for _ in ' '*~-n:
    a, b = map(int, input().split())
    E[a-1] += b-1,
    E[b-1] += a-1,
D = [[0]*2 for _ in ' '*n]
V = [0]*n


def f(x):
    D[x][1] = A[x]
    for i in E[x]:
        if not D[i][1]:
            D[x][0] += f(i)
            D[x][1] += D[i][0]
    V[x] = D[x][1] > D[x][0]
    return max(D[x])


print(f(0))
print(*[1+i for i in range(n)if V[i]])
