D = [1, 5, 10, 20, 50, 100]
*A, = map(int, input().split())
print(D[max((D[i]*A[i], i)for i in range(6))[1]])
