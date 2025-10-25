f = lambda: [*map(int, input().split())]
while sum(A := f()):
    n, m = A
    A = f()
    B = f()
    C = [0] * 10
    for i in range(n):
        for j in range(m):
            x = A[i] * B[j]
            while x:
                C[x % 10] += 1
                x //= 10
    print(*C)
