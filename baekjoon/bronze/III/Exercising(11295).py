*A, _ = map(int, open(0).read().split())
i = 1
while A:
    l, n, *A = A
    A, B = A[n:], A[:n]
    print('User', i)
    for b in B:
        print(f'{b*l/10**5:.5f}')
    i += 1
