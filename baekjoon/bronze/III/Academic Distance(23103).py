_, l, *L = open(0)
a, b = map(int, l.split())
A = 0
for l in L:
    x, y = map(int, l.split())
    A += abs(x-a)+abs(y-b)
    a, b = x, y
print(A)
