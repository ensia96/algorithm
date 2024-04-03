n, a, b, c, *A = map(int, open(0).read().split())
x, y = (A[-1]if A else c), b-a
print([x*c//b, x+y][y == c-b])
