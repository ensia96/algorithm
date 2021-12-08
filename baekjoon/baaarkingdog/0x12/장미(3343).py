n, a, b, c, d = map(int, input().split())
a, b, c, d = [(c, d, a, b), (a, b, c, d)][b*c > a*d]
A = 10**18
for i in range(a):
    if n > 0:
        A, n = min(d*i+(n//a+bool(n % a))*b, A), n-c
print(A)
