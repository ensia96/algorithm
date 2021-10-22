d, A = lambda: map(int, input().split()), 0
n, m, l = d()
r, a, b = sorted([0, *d(), l-1]), 0, l-1
while a <= b:
    c, k = (a+b)//2, 0
    for i in range(1, len(r)):
        d = r[i]-r[i-1]
        k += (d-1)//c if d > c else 0
    a, b, A = [(a, c-1, c), (c+1, b, A)][k > m]
print(A)
