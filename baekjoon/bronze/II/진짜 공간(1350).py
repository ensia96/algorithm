n, *A, c = map(int, open(0).read().split())
print(sum(-(a//-c)for a in A)*c)
