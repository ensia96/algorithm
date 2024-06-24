n, c, *A = map(int, open(0).read().split())
x = y = n
for i in range(c):
    a, b = A[i*2:i*2+2]
    if a < y and b < x:
        y, x = [(a, x), (y, b)][x*a < y*b]
print(y*x)
