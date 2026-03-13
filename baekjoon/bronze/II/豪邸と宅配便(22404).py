_, m, t, *A = map(int, open(0).read().split())
X = [1] * t
for a in A:
    X[a - m:a + m] = [0] * 2 * m
print(sum(X))
