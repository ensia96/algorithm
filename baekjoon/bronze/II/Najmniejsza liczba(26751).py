a, b, c = sorted(input()[::2])
print((a + b + c, b + a + c, c + a + b)[(a < '1') + (b < '1')])
