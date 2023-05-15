_, X, *L = open(0)
L += a,
a, b = map(int, a.split())
A = 0
for l in L:
    x, y = map(int, l.split())
    A += x == a and abs(y-b) or abs(x-a)
    a, b = x, y
print(A)
