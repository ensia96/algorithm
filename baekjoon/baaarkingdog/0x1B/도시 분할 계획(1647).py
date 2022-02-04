import sys
I = sys.stdin.readline
n, m = map(int, input().split())
R, H = [*range(n+1)], [0]*-~n
A = E = 0


def f(x):
    if R[x] != x:
        R[x] = f(R[x])
    return R[x]


for w, i, j in sorted((*map(int, input().split()[::-1]),)for _ in ' '*m):
    if not E-n+2:
        break
    i, j = f(i), f(j)
    if i == j:
        continue
    if H[i] < H[j]:
        i, j = j, i
    R[j], H[i], A, E = R[i], H[i]+1, A+w, E+1
print(A)
