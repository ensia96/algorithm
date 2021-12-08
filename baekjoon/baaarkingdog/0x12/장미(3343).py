n, a, b, c, d = map(int, input().split())
print(min(n//a*b+bool(n % a)*min(b, (n % a//c+bool(n % a % c) or 1)*d),
      n//c*d+bool(n % c)*min((n % c//a+bool(n % c % a) or 1)*b, d)))
