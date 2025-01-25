f = lambda x: chr(x + 97 - 1)
a, b = map(int, input().split())
x, y = divmod(b, 26)
print("SN", str(a) + (f(x) if x else "") + f(y - (not x) * 32))
