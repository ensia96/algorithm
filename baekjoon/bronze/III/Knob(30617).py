n, *A = map(int, open(0).read().split())
T = [*zip(A[::2], A[1::2])]
t = 0
for i in range(n):
    a, b = T[i]
    t += a*(a == b)
    j = i > 0
    c, d = T[i-1]
    t += j*a*(a == c)
    t += j*b*(b == d)
print(t)
