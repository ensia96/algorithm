import sys
I = sys.stdin.readline
l, A = lambda x: map(int, input().split()[::x]), 0
n, m, k = l(1)
G = [*l(1)]
g = len(G)
E = [(*l(-1),)for _ in ' '*m]
for i in range(g):
    E += (0, G[i], n+i+1),
    for j in range(i+1, g):
        E += (0, n+i+1, n+j+1),
E.sort()
R, L, e = [*range(n+g+1)], [0]*(n+g+1), 0


def f(x):
    if R[x] != x:
        R[x] = f(R[x])
    return R[x]


for w, i, j in E:
    i, j = f(i), f(j)
    if i == j:
        continue
    A, e = A+w, e+1
    if e == n+g-1:
        break
    if L[i] < L[j]:
        i, j = j, i
    R[j], L[i] = R[i], L[i]+1
print(A)
