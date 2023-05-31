n, *A = map(int, open(0).read().split())
print(+(sum(a % 2 for a in A) == -(n//-2)))
