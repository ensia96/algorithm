l, r = lambda: map(int, input().split()), range
n, m = l()
A = [*l()]
C = [*l()]
k = sum(C)+1
D = [0]*k
for i in r(n):
    for j in r(k-1, C[i]-1, -1):
        D[j] = max(D[j], D[j-C[i]]+A[i])
for j in r(k):
    if D[j] >= m:
        exit(print(j))
