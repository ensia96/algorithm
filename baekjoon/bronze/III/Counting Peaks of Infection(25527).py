*A, _ = map(int, open(0).read().split())
while A:
    n, *A = A
    A, B = A[n:], A[:n]
    print(sum(B[i+1] < B[i] > B[i-1]for i in range(1, n-1)))
