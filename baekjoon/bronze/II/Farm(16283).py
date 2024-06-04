a, b, n, w = map(int, input().split())
A = [(i, n-i)for i in range(1, n)if (n-i)*b+a*i == w]
print(*A[0]if 1 == len(A)else [-1])
