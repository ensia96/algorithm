import decimal
a, b, c, d = map(int, input().split())
print(int(decimal.Decimal((min(a, b)+min(c, d))**.5)))
