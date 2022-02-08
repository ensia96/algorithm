import sys
I = sys.stdin.readline
n = int(I())
P = [(*map(int, I().split()), i)for i in range(n)]
R, E = [i for i in range(n)], []


def f(x):
    if R[x] != x:
        R[x] = f(R[x])
    return R[x]


for j in range(3):
    P.sort(key=lambda x: x[j])
    for i in range(1, n):
        E += (abs(P[i][j]-P[i-1][j]), P[i-1][3], P[i][3]),
E.sort()
a = e = 0
for w, i, j in E:
    i, j = f(i), f(j)
    if i == j:
        continue
    a, e, R[j] = a+w, e+1, i
    if e == n-1:
        break
print(a)
