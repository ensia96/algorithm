n, *A = map(int, open(0).read().split())
t = [0]*2
for i, j in zip(A[1:], A):
    t[i > j] += i-j
print(-t[0], t[1])
