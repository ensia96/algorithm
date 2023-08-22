n, *A = map(int, open(0).read().split())
A = [a % 2 for a in A]
print(2, +(A.count(1)*2 >= n))
