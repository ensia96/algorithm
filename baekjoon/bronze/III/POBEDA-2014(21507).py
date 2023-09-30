import decimal
a, b, c, d = map(decimal.Decimal, input().split())
print(int((min(a, b)+min(c, d)).sqrt()))
