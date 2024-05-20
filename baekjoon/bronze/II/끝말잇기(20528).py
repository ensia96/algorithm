n, *A = open(0).read().split()
print(int(len({a[0]for a in A}) < 2))
