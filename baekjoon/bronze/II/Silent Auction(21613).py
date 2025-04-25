_, *A = open(0)
print(A[::2][(t := [*map(int, A[1::2])]).index(max(t))][:-1])
