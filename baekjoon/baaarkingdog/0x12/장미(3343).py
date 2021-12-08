n, a, b, c, d = map(int, input().split())
if a*d < b*c:
    a, b, c, d = c, d, a, b
print(min(d*i+((n-c*i)//a+bool((n-c*i) % a))*b for i in range(min(n//c, a)+1)))
