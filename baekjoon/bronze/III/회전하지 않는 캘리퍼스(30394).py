_, *A = map(int, open(0).read().split())
a = A[1::2]
print(max(a)-min(a))
