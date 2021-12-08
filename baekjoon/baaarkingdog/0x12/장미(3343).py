n, a, b, c, d = map(int, input().split())
a, b, c, d = [(a, b, c, d), (c, d, a, b)][b*c > a*d]
print(min(d*i + ((n-c*i)//a+bool((n-c*i) % a))*b for i in range(a) if c*i < n))
