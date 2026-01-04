_, i, *L = map(int, open(0).read().split())
print(i, *[(i := l)for l in L if i <= l])
