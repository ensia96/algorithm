a, b, c, d, e = map(int, open(0))
x, y = divmod(e, a+b)
n = (a-b)*x+[y, a-y][y > a]
x, y = divmod(e, c+d)
b = (c-d)*x+[y, c-y][y > c]
print(['NBiykrkoyn'[n < b::2], 'Tie'][n == b])
