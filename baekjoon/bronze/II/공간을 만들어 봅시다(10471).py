w, p, *A = map(int, open(0).read().split())
A = [0, *A, w]
print(*sorted({abs(a - b) for a in A for b in A}))
