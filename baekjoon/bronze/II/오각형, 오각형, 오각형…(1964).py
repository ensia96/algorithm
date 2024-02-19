x, y = 1, 4
for _ in ' '*int(input()):
    x, y = (x+y) % 45678, y+3
print(x)
