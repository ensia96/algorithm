import collections as c
n = int(input())+1
C, D = [[]for _ in ' '*n], [0]*n
A = [[0]*n for _ in ' '*n]
for _ in ' '*int(input()):
    x, y, k = map(int, input().split())
    C[y] += (x, k),
    D[x] += 1
Q = c.deque(i for i in range(1, n)if not D[i])
while Q:
    c = Q.popleft()
    for p, x in C[c]:
        if sum(A[c]):
            for i in range(1, n):
                A[p][i] += A[c][i]*x
        else:
            A[p][c] += x
        D[p] -= 1
        if not D[p]:
            Q.append(p)
for i in range(1, n):
    if A[n-1][i]:
        print(i, A[n-1][i])
