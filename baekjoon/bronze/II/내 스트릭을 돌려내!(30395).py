n, *A = map(int, open(0).read().split())
f = -2
M = m = 0
for i in range(n):
    if A[i] > 0:
        m += 1
    elif f < i - 2:
        f = i
    else:
        m = 0
    M = max(M, m)
print(M)
