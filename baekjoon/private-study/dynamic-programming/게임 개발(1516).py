n = int(input())+1
D, E = [0]*-~n, [0]
N = range(1, n)
for i in N:
    c, *A = map(int, input().split())
    D[i] = c
    E += A,
for i in N:
    D[i] += max(D[e]for e in E[i])
    print(D[i])
