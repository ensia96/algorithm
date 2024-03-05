n, *A = map(int, open(0).read().split())
t = []
for i in range(n):
    t += -~i*A[i]-sum(t),
print(*t)
