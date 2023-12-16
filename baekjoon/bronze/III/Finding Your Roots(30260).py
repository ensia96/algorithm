n, *A = map(int, open(0).read().split())
for i in range(n):
    n, m, *A = A
    T, t, A = A[:m], 1, A[m:]
    while T[n-1]:
        n, t = T[n-1], t+1
    print(f'Data Set {i+1}:\n{t}\n')
