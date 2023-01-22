a, b, c = sorted(map(int, input().split()))
print(1 if c**2 == a**2+b**2 else 2 if a == b == c else 0)
