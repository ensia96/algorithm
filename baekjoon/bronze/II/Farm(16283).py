a, b, n, w = map(int, input().split())
A = [i for i in range(1, n)if (n-i)*b+a*i == w]
print(*[A[0], n-A[0]]if len(A) == 1 else [-1])
