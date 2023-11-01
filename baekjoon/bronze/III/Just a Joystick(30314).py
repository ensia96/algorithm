n, a, b = open(0).read().split()
A = 0
for i in range(int(n)):
    x, y = sorted([ord(a[i])-64, ord(b[i])-64])
    A += min(26+x-y, y-x)
print(A)
