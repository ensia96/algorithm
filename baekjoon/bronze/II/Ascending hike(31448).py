n, *A = map(int, open(x := 0).read().split())
print(max([x := (x + j - i) * (j > i)for i, j in zip(A, A[1:])]))
