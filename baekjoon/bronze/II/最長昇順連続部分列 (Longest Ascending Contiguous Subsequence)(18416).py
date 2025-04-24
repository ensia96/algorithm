n, *A = map(int, open(0).read().split())
t = m = 1
for i in range(n-1):
    m = max(m, t := [t+1, 1][A[i] > A[i+1]])
print(m)
