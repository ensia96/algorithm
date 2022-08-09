import sys
import collections as C
sys.setrecursionlimit(650001)


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


n, m = map(int, input().split())
N = range(n)
E = [[]for i in N]
R = [[]for i in N]
V = [0]*n
S = []
H = [-1]*n
G = []
for i in range(m):
    a, b = map(int, input().split())
    E[a-1].append(b-1)
    R[b-1].append(a-1)
W = [int(input())for i in N]
for i in N:
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
s, p = map(int, input().split())
s -= 1
del E, R
Q = C.deque([H[s]])
D = [0]*k
D[H[s]] = M[H[s]]
while Q:
    x = Q.popleft()
    for n in G[x]:
        if D[n] < D[x]+M[n]:
            D[n] = D[x]+M[n]
            Q.append(n)
print(max(D[H[r-1]]for r in map(int, input().split())))
