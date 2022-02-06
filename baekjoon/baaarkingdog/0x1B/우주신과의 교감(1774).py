l, t = lambda: map(int, input().split()), lambda a, b: (a**2+b**2)**.5
n, m = l()
n += 1
L = {i: (*l(),)for i in range(1, n)}
Q = [(0, *l())for _ in ' '*m]
for i in range(1, n):
    for j in range(i+1, n):
        a, b = L[i]
        c, d = L[j]
        Q.append((t(a-c, b-d), i, j))
Q.sort()
P, L = [*range(n)], [0]*n
A = E = 0


def f(x):
    if P[x] != x:
        P[x] = f(P[x])
    return P[x]


for w, i, j in Q:
    i, j = f(i), f(j)
    if i == j:
        continue
    A, E = A+w, E+1
    if E == n-2:
        break
    if L[i] < L[j]:
        i, j = j, i
    P[j], L[i] = P[i], L[i]+1
print(f"{A:.2f}")
