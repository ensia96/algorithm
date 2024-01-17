n, m = map(int, [*open(0)])
A = [i*i for i in range(101)if n <= i*i <= m]
for i in [sum(A), A[0]]if A else [-1]:
    print(i)
