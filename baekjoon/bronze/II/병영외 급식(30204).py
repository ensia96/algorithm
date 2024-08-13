n, m, *A = map(int, open(0).read().split())
print(+(sum(A) % m < 1))
