import math
n, a, b, c, d = map(int, input().split())
g = math.gcd(a, c)
q, m = divmod(n, g)
print(min(q*g//a*b, q*g//c*d)+min((m//a or 1)*b, (m//c or 1)*d))
