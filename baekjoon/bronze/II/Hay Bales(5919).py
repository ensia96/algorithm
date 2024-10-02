n, *A = map(int, open(0).read().split())
print(sum(abs(sum(A) // n - a) for a in A) // 2)
