n, m = map(int, input().split())
E = [[]for _ in ' '*-~n]
F = [[]for _ in ' '*-~n]
for _ in ' '*m:
    a, b = map(int, input().split())
    E[a] += b,
W = [0]+[int(input())for _ in ' '*n]
s, p = map(int, input().split())
R = {*map(int, input().split())}

y = 0
S = []
P = []
Q = []
A = [0]*-~n
B = [-1]*-~n
C = [1]*-~n
M = [0]*-~n
N = [0]*-~n
O = [0]*-~n
U = [0]*-~n
I = [0]*-~n


def f(x):
    global y, S, P
    X = B[x] = y
    y += 1
    S += x,
    for e in E[x]:
        if B[e] == -1:
            X = min(X, f(e))
        elif C[e]:
            X = min(X, B[e])
    if X == B[x]:
        T = []
        while 1:
            t = S.pop()
            T += t,
            C[t], N[t] = 0, len(P)
            if t == x:
                break
        P += T,
    return X


for i in range(1, n+1):
    1+B[i] or f(i)
for i in range(1, n+1):
    O[N[i]] += W[i]
    if i in R:
        U[N[i]] = 1
    for j in E[i]:
        if N[i]-N[j]:
            F[N[i]] += N[j],
            I[N[j]] += 1
for i in range(len(P)):
    M[i] = O[i]
    if I[i] == 0:
        Q += i,
A[N[s]] = 1
while Q:
    q = []
    for x in Q:
        for a in F[x]:
            I[a] -= 1
            if A[x]:
                M[a], A[a] = max(M[a], M[x]+O[a]), 1
            if I[a] == 0:
                q += a,
    Q = q
print(max(M[i]for i in range(len(P))if A[i]*U[i]))
