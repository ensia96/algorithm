n, m = map(int, input().split())
A = [0] * n * m
for i in range(n):
    for j in range(m):
        A[i + j] += 1
for i in range(n * m):
    if A[i] == max(A):
        print(i + 2)
