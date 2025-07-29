a, b, c, d, e = map(int, open(0))
x, y = divmod(e, a+b)
n = x*(a-b)+[y, a+a-y][y > a]
x, y = divmod(e, c+d)
b = x*(c-d)+[y, c+c-y][y > c]
print(["NBiykrkoyn"[b > n::2], "Tied"][n == b])
