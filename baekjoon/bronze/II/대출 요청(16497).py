D = [0] * 33
_, *A, k = map(int, open(0).read().split())
for a, b in zip(A[::2], A[1::2]):
    for i in range(a - 1, b):
        D[i] += 1
print(1 ^ (max(D) > k))
