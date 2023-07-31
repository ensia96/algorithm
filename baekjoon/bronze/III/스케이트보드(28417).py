n, *A = map(int, open(0).read().split())
t = 0
for i in range(n):
    _A = A[i*7:-~i*7]
    t = max(t, max(_A[:2])+sum(sorted(_A[2:])[-2:]))
print(t)
