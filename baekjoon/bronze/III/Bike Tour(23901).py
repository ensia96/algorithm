n, *A = map(int, open(0).read().split())
t = 0
while A:
    t += 1
    n, *A = A
    A, B = A[n:], A[:n]
    print(f"Case #{t}:", sum([B[i] < B[i+1] > B[i+2]for i in range(n-2)]))
