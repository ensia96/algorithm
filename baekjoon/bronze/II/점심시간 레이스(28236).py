n, m, k, *A = map(int, open(0).read().split())
print(min((A[2 * i] - A[2 * i + 1], i + 1) for i in range(k)))
