n, a, b, c, d = map(int, input().split())
A = 10**18
for i in range(a+1):
    if n > 0:
        A, n = min(d*i+(n//a+bool(n % a))*b, A), n-c
print(A)
