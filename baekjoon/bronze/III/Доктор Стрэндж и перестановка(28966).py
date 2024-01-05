n, *A = map(int, open(0).read().split())
T = [-~i for i in range(n)if -~i % 2 != A[i] % 2]
print(*[[[-1, -1], '13'][not T and n > 2], T][len(T) == 2])
