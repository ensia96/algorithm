n, *A = map(int, open(0).read().split())
print(*[1]+[2+A.index(i)for i in range(n-1)])
