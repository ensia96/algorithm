a, b, c, d = map(int, input().split())
x, y = 60*c+d, 60*a+b
z = x-y+1440*(x < y)
print(z, z//30)
