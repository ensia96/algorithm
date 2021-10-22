d, A = lambda: map(int, input().split()), 0
n, m, l = d()
r, a, b = sorted([0, *d(), l]), 1, l
while a <= b:
    c, k = (a+b)//2, 0
    for i in range(1, n+2):
        k += (r[i]-r[i-1]-1)//c
    a, b, A = [(a, c-1, c), (c+1, b, A)][k > m]
print(A)
