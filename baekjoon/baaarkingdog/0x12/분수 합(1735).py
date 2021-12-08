g, i = lambda a, b: (a == 0)*b or g(b % a, a), input
a, b = map(int, i().split())
A, B = map(int, i().split())
x, y = a*B+A*b, b*B
z = g(x, y)
print(x//z, y//z)
