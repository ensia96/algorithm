from decimal import Decimal
a, b, c = map(int, input().split())
result = Decimal(a)*Decimal(b)/Decimal(c)
print(f"{result:.6f}")
