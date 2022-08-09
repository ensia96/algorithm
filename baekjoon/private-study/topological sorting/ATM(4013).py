from collections import deque
import sys
sys.setrecursionlimit(650001)
I = sys.stdin.readline
L, S = lambda: map(int, I().split()), []


def f(x):
    V[x] = 1
    for a in E[x]:
        V[a] or f(a)
    S.append(x)


def r(x, y):
    H[x] = y
    M[y] += W[x]
    for a in R[x]:
        if H[a] == -1:
            r(a, y)
        elif H[x]-H[a]:
            G[H[a]].append(H[x])


n, m = L()
E = [[]for i in range(n)]
R = [[]for i in range(n)]
V = [0]*n
S = []
H = [-1]*n
G = []
for i in range(m):
    a, b = L()
    E[a-1].append(b-1)
    R[b-1].append(a-1)
W = [int(I())for i in range(n)]
for i in range(n):
    V[i] or f(i)
M = []
k = 0
while S:
    x = S.pop()
    if H[x] == -1:
        G.append([])
        M.append(0)
        r(x, k)
        k += 1
s, p = L()
s -= 1
del E, R
Q = deque([H[s]])
D = [0]*k
D[H[s]] = M[H[s]]
while Q:
    x = Q.popleft()
    for n in G[x]:
        if D[n] < D[x]+M[n]:
            D[n] = D[x]+M[n]
            Q.append(n)
A = 0
for r in L():
    A = max(A, D[H[r-1]])
print(A)
