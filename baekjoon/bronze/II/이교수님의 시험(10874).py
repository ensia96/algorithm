for l in [*open(y := 0)][1:]:
    y += 1
    *A, = map(int, l.split())
    sum(A[i] == (i % 5+1)for i in range(10)) > 9 and print(y)
