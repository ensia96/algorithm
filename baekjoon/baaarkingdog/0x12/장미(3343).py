n, a, b, c, d = map(int, input().split())
if a*d <= b*c:
    a, b, c, d = c, d, a, b
A = b*(n//a+bool(n % a))
for i in range(a):
    if n-c*i > 0:
        A = min(A, d*i+((n-c*i)//a+bool((n-c*i) % a))*b)
print(A)
