D = [0] * 33
_, *A, k = map(int, open(0).read().split())
for I in zip(A[::2], A[1::2]):
    for i in range(*I):
        D[i] += 1
print(1 ^ (max(D) > k))
