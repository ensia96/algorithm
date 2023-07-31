_, *A = map(int, open(0).read().split())
t = 0
while A:
    _A, A = A[:7], A[7:]
    t = max(t, max(_A[:2])+sum(sorted(_A[2:])[-2:]))
print(t)
