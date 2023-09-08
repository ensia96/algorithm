*A, _ = map(int, open(0).read().split())
while A:
    n, *A = A
    for i in range(n):
        T = [a < 128 for a in A[i*5:-~i*5]]
        print('*'if 1 < T.count(1)else 'ABCDE'[T.index(1)])
    A = A[n*5:]
