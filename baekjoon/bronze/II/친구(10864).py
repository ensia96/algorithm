n, m, *A = map(int, open(0).read().split())
D = {i+1: []for i in range(n)}
for a, b in zip(A[::2], A[1::2]):
    D[a] += b,
    D[b] += a,
for i in D:
    print(len(D[i]))
