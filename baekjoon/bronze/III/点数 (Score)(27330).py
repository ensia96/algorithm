n, *A = map(int, open(0).read().split())
t = 0
for a in A[:n]:
    t = (t+a)*(a not in A[n+1:])
print(t)
