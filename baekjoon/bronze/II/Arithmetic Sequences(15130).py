R = range(10)
*A, = map(int, input().split())
a, b = [i for i in R if A[i]]
x, y = divmod(A[b]-A[a], b-a)
print(*[[A[a]-x*(a-i)for i in R], [-1]][y > 0])
