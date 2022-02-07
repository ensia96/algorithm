import sys
I = sys.stdin.readline
l, A = lambda x: map(int, input().split()[::x]), 0
n, m, k = l(1)
R, L, e = [*range(n+1)], [0]*(n+1), 0
for i in l(1):
    R[i] = 0


def f(x):
    if R[x] != x:
        R[x] = f(R[x])
    return R[x]


for w, i, j in sorted((*l(-1),)for _ in ' '*m):
    i, j = f(i), f(j)
    if i == j:
        continue
    A, e = A+w, e+1
    if e == n-1:
        break
    if L[i] < L[j]:
        i, j = j, i
    R[j], L[i] = R[i], L[i]+1
print(A)
