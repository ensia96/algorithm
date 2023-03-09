r = range(9)
A = [[*map(int, input().split())]for i in r]
a, b, c = max((A[i][j], i+1, j+1)for i in r for j in r)
print(a)
print(b, c)
