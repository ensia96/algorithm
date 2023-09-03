p = print()
for l in [*open(0)][1:]:
    *A, _ = l
    n = len(A)-2
    p(''.join(A))
    for i in range(n):
        p(A[i+1], ' '*(n-2), A[-i-2])
    p(''.join(A)[::-1])
