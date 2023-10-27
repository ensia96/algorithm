n, m, *A = map(int, open(0).read().split()+[0])
x = y = 0
for i in range(n):
    y += A[i]
    if y > m:
        x += 1
        y = 0
    print(x)
