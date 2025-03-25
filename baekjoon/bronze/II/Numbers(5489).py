_, *A = map(int, open(0))
print(min([[-A.count(a), a] for a in A])[1])
