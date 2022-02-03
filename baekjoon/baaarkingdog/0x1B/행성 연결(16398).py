I, R = input, range


def f(x):
    if P[x] != x:
        P[x] = f(P[x])
    return P[x]


n = int(I())
C = [[*map(int, I().split())]for _ in ' '*n]
P, A, L = [*R(n)], 0, [0]*n
for w, i, j in sorted((C[i][j], i, j)for i in R(n)for j in R(i+1, n)):
    i, j = f(i), f(j)
    if i == j:
        continue
    if L[i] < L[j]:
        i, j = j, i
    P[j], L[i], A = i, L[i]+1, A+w
print(A)
