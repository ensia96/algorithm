n, a, b, c, d = map(int, input().split())
print(min(n//a*b+min(b, (n % a//c or 1)*d), n//c*d+min((n % c//a or 1)*b, d)))
