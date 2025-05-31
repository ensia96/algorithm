_, *A, h = map(int, open(0).read().split())
print(min((h % a, a)for a in A)[1])
