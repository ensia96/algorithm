a, b, *A = map(int, open(0).read().split())
x, y = sum(A), a-b
print((x-3*y)/a, (x+3*y)/a)
