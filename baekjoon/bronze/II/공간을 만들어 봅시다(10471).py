w, p, *A = map(int, open(0).read().split())
A = [0, *A, w]
print(*sorted({abs(A[i] - A[j]) for i in range(p + 2) for j in range(i + 1, p + 2)}))
