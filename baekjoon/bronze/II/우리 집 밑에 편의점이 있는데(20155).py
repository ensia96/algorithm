n, m, *A = map(int, open(0).read().split())
print(max(map(A.count, range(1, m + 1))))
