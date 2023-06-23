n, *A = open(0).read().split()
x = 1
for a in A:
    x += a != n
    n = a
print(x)
