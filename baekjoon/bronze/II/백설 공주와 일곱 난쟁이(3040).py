*A, = map(int, open(0))
S, R = sum(A)-100, range(9)
for i in R:
    for j in range(i):
        if S == A[i]+A[j]:
            for k in {*R}-{i, j}:
                print(A[k])
