n, *A = map(int, open(0).read().split())
t = []
for i in range(n):
    for j in range(n):
        a = A[i*n+j]
        if i == j:
            if a:
                t += 1,
        else:
            if a < 1:
                t += 2,
            if a != A[j*n+i]:
                t += 3,
            for k in range(n):
                if a+A[j*n+k] < A[i*n+k]:
                    t += 4,
print(t, min(t or [0]))
