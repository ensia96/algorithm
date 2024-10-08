n, m, *A = map(int, open(0).read().split())
print(max([A[i + n] - (i < n and A[i]) for i in range(m)] + [0]))
