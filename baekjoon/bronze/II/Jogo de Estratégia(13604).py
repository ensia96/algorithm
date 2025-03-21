j, r, *A = map(int, open(0).read().split())
print(sorted((sum(A[i::j]), i) for i in range(j))[-1][1] + 1)
