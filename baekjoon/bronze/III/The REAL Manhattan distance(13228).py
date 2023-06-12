n, *A = map(int, open(0).read().split())
for i in range(n):
    a, b, c, x, y, z = A[i*6:-~i*6]
    print(c+abs(a-x)+abs(b-y)+z)
